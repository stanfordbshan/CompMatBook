#!/usr/bin/env bash
# For the four-atom cubic POSCAR shown in note 04.3.3.
set -euo pipefail
export LC_ALL=C
shopt -s nullglob

mode=${1:?Usage: scan_ni.sh prepare|run|collect scan_dir [start stop step]}
root=${2:?Specify a scan directory}
shift 2

if [[ "$mode" == prepare ]]; then
    # Integer hundredths of an Angstrom avoid float accumulation.
    start=${1:-300}
    stop=${2:-400}
    step=${3:-5}
    if ! (( step > 0 && start > 0 && stop >= start && (stop - start) % step == 0 )); then
        echo "Invalid scan range" >&2
        exit 2
    fi
    for file in INCAR KPOINTS POSCAR POTCAR; do
        test -s "$file"
    done
    mkdir -- "$root"
    for (( n=start; n<=stop; n+=step )); do
        a=$(printf '%d.%02d' "$((n / 100))" "$((n % 100))")
        point="$root/a${a/./p}"
        mkdir -- "$point"
        cp INCAR KPOINTS POTCAR "$point/"
        awk -v a="$a" 'NR==2 {$0=a} {print}' POSCAR > "$point/POSCAR"
    done
    exit
fi

points=("$root"/a*p*)
if (( ${#points[@]} == 0 )); then
    echo "No scan points in $root" >&2
    exit 2
fi

if [[ "$mode" == run ]]; then
    : "${VASP_EXE:?Set VASP_EXE to the absolute path to vasp_std}"
    [[ "$VASP_EXE" == /* && -x "$VASP_EXE" ]]
    launcher=(mpirun -np "${MPI_RANKS:-4}")
    if [[ "${VASP_USE_SLURM:-0}" == 1 ]]; then
        : "${SLURM_JOB_ID:?Run inside a Slurm allocation when VASP_USE_SLURM=1}"
        launcher=(srun --mpi=pmix --cpu-bind=threads
                  -n "${MPI_RANKS:-${SLURM_NTASKS:-1}}" -c "${SLURM_CPUS_PER_TASK:-1}")
    fi
    for point in "${points[@]}"; do
        if [[ -e "$point/OUTCAR" || -e "$point/vasp.out" ]]; then
            echo "Refusing to overwrite existing output in $point" >&2
            exit 2
        fi
    done
    for point in "${points[@]}"; do
        (cd "$point"; "${launcher[@]}" "$VASP_EXE" < /dev/null > vasp.out)
    done
elif [[ "$mode" == collect ]]; then
    rows=()
    for point in "${points[@]}"; do
        if ! grep -Fq 'aborting loop because EDIFF is reached' "$point/OUTCAR" ||
           ! grep -Fq 'General timing and accounting' "$point/OUTCAR"; then
            echo "Missing SCF convergence or completion marker: $point" >&2
            exit 2
        fi
        a=$(awk 'NR==2 {printf "%.2f", $1}' "$point/POSCAR")
        e=$(awk '/energy\(sigma->0\)/ {e=$NF}
            END {if (e=="") exit 1; printf "%.8f", e}' "$point/OUTCAR")
        rows+=("$a,$e")
    done
    printf '%s\n' 'lat,ene' "${rows[@]}"
else
    echo "Unknown mode: $mode" >&2
    exit 2
fi
