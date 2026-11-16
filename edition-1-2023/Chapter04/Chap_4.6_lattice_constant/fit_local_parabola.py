"""Fit the bottom of the fcc Ni energy well and render teaching figures."""
import argparse
import csv
from itertools import product
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np


def fit_window(a, energy, center, reference, label):
    x = a - center
    y = energy - reference
    A, B, C = np.polyfit(x, y, 2)
    if A <= 0:
        raise ValueError(f"{label}: no convex minimum")
    a0 = center - B / (2 * A)
    if not a[0] < a0 < a[-1]:
        raise ValueError(f"{label}: minimum outside fit interval")
    residual = np.polyval((A, B, C), x) - y
    return {
        "window": label, "points": len(a), "a_left_A": a[0], "a_right_A": a[-1],
        "a0_A": a0, "A_eV_per_cell_A2": A, "B_eV_per_cell_A": B,
        "C_eV_per_cell": C, "rms_meV_per_atom": 250 * np.sqrt(np.mean(residual**2)),
    }


def draw_cell(path):
    corners = np.array(list(product((0.0, 1.0), repeat=3)))
    faces = np.full((6, 3), 0.5)
    for axis in range(3):
        faces[2 * axis:2 * axis + 2, axis] = (0, 1)

    fig = plt.figure(figsize=(6.8, 5.3), layout="constrained")
    ax = fig.add_subplot(projection="3d")
    for i, u in enumerate(corners):
        for v in corners[i + 1:]:
            if np.count_nonzero(u - v) == 1:
                ax.plot(*np.vstack((u, v)).T, color="#606060", lw=1.2)
    ax.scatter(*corners.T, s=135, color="#c0e0f0", edgecolors="#31556a",
               depthshade=False, label="8 corners: 1/8 each")
    ax.scatter(*faces.T, s=165, color="#007d9c", edgecolors="white",
               depthshade=False, label="6 face centers: 1/2 each")
    ax.text(0.5, -0.13, -0.07, r"$a$", color="#202020", fontsize=18)
    ax.set(xlim=(-0.08, 1.08), ylim=(-0.15, 1.08), zlim=(-0.08, 1.08))
    ax.set_box_aspect((1.16, 1.23, 1.16))
    ax.set_proj_type("ortho")
    ax.view_init(elev=22, azim=-58)
    ax.set_axis_off()
    ax.set_title("FCC conventional cell: 4 atoms after sharing", pad=10)
    ax.legend(loc="lower center", bbox_to_anchor=(0.5, -0.01), ncol=2, frameon=False)
    fig.savefig(path, dpi=220)
    plt.close(fig)


def draw_energy(path, a, energy, i, fits):
    ref = energy[i]
    center = a[i]
    local = fits["5 points"] if "5 points" in fits else fits["3 points"]
    lo, hi = local["a_left_A"], local["a_right_A"]
    selected = (a >= lo) & (a <= hi)
    fig, (wide, near) = plt.subplots(1, 2, figsize=(12, 4.8), layout="constrained")
    wide.axvspan(lo, hi, color="#c0e0f0", alpha=0.52, label="Local fit window")
    wide.plot(a, (energy - ref) / 4, "o-", color="#31556a", ms=4, label="VASP points")
    grid = np.linspace(a[0], a[-1], 300)
    bad = fits["full scan"]
    keys = ("A_eV_per_cell_A2", "B_eV_per_cell_A", "C_eV_per_cell")
    wide.plot(grid, np.polyval([bad[k] for k in keys], grid - center) / 4,
              "--", color="#606060", lw=1.25, label="Full-range parabola (poor)")
    wide.set(title="(a) Full scan: asymmetric energy well",
             xlabel="Lattice constant (Å)", ylabel="Relative energy (eV/atom)")
    wide.legend(loc="upper right", frameon=False, fontsize=10)
    grid = np.linspace(lo, hi, 250)
    coeff = [local[k] for k in keys]
    near.plot(grid, 250 * np.polyval(coeff, grid - center), color="#007d9c", lw=2,
              label=f"Local quadratic ({local['points']} points)")
    near.scatter(a[selected], 250 * (energy[selected] - ref), color="#202020",
                 s=32, zorder=3, label="VASP points in fit")
    y0 = 250 * np.polyval(coeff, local["a0_A"] - center)
    near.vlines(local["a0_A"], y0, 0, color="#007d9c", ls=":", lw=1.2)
    near.scatter([local["a0_A"]], [y0],
                 color="#007d9c", marker="D", s=35, zorder=4,
                 label=f"Fitted minimum: {local['a0_A']:.4f} Å")
    near.scatter([center], [0], facecolors="none", edgecolors="#202020",
                 s=100, zorder=5, label=f"Lowest sampled point: {center:.2f} Å")
    near.set(title="(b) Valley bottom: local fit",
             xlabel="Lattice constant (Å)", ylabel="Relative energy (meV/atom)")
    near.legend(loc="upper right", frameon=False, fontsize=9)
    for ax in (wide, near):
        ax.spines[["top", "right"]].set_visible(False)
        ax.set_axisbelow(True)
        ax.grid(axis="y", alpha=0.15)
    fig.savefig(path, dpi=200)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("csv_file", type=Path, help="lat,ene CSV: Å, eV per 4-atom cell")
    parser.add_argument("--out", type=Path, default=Path("ni_fit"))
    args = parser.parse_args()
    data = np.loadtxt(args.csv_file, delimiter=",", skiprows=1, ndmin=2)
    if data.shape[1] != 2 or len(data) < 3 or not np.all(np.isfinite(data)):
        raise ValueError("Expected at least three finite lat,ene rows")
    a, energy = data[np.argsort(data[:, 0])].T
    if np.any(np.diff(a) <= 0):
        raise ValueError("Duplicate lattice constants")
    i = int(np.argmin(energy))
    if i in (0, len(a) - 1):
        raise ValueError("Sampled minimum is at an endpoint: extend the scan")

    fits = {}
    for half in (1, 2, 3, 4):
        if i - half >= 0 and i + half < len(a):
            s = slice(i - half, i + half + 1)
            label = f"{2 * half + 1} points"
            fits[label] = fit_window(a[s], energy[s], a[i], energy[i], label)
    # Full-range fit is included only to demonstrate the bias of a broad parabola.
    fits["full scan"] = fit_window(a, energy, a[i], energy[i], "full scan")
    args.out.mkdir(parents=True, exist_ok=True)
    summary = args.out / "parabolic_fit_summary.csv"
    with summary.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(next(iter(fits.values()))))
        writer.writeheader()
        writer.writerows(fits.values())
    print(f"Lowest sampled point: a={a[i]:.2f} A, E={energy[i]:.8f} eV/cell")
    for fit in fits.values():
        print(f"{fit['window']:>9}: a0={fit['a0_A']:.6f} A, "
              f"rms={fit['rms_meV_per_atom']:.3f} meV/atom")
    plt.rcParams.update({"font.size": 12, "axes.titlesize": 13, "axes.labelsize": 12})
    draw_cell(args.out / "ch04_ni_fcc_conventional_cell.png")
    draw_energy(args.out / "ch04_ni_local_parabola.png", a, energy, i, fits)


if __name__ == "__main__":
    main()
