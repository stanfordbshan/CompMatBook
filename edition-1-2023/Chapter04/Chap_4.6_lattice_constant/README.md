# FCC Ni lattice-constant example

This folder includes the 3.50-angstrom static inputs and the 21-point scan
from the lattice-constant tutorial. The original `lattice_constant.sh` is
retained for reference; the commands below use `scan_ni.sh`.

## Fit the supplied results

No VASP installation or pseudopotential is needed for this step. Use Python
with NumPy and Matplotlib:

```bash
python fit_local_parabola.py ni_fcc_energy.example.csv --out ni_fit
```

The sample CSV is from the tutorial's 21-point VASP 6.6.1 scan. Its columns
are lattice constant in angstroms and `energy(sigma->0)` in eV per
four-atom cell. The three- and five-point fits both give about 3.52 angstroms.

## Run a fresh scan

Work in a separate calculation directory with copies of `INCAR`, `POSCAR`,
`KPOINTS`, and `scan_ni.sh`. Supply your own licensed `POTCAR` from the VASP
PAW PBE `Ni` dataset (`PAW_PBE Ni 02Aug2007`, not `Ni_pv`). Do not commit
the pseudopotential or the generated run directories.

With Bash, VASP, and an MPI launcher available, run from that directory:

```bash
export VASP_EXE=/absolute/path/to/vasp_std
export OMP_NUM_THREADS=1
export MPI_RANKS=2
bash scan_ni.sh prepare lesson_coarse 300 400 5
bash scan_ni.sh run lesson_coarse
bash scan_ni.sh collect lesson_coarse > ni_fcc_energy.csv
```

`prepare` changes only line 2 of `POSCAR` between points. The integers
`300 400 5` mean 3.00 to 4.00 angstroms in 0.05-angstrom steps. Run
the MPI step on allocated compute resources. `collect` checks electronic
convergence and normal termination before reporting energies.
