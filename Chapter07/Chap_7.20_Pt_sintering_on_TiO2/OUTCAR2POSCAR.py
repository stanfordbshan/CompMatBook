# 功能：从VASP-AIMD计算输出的OUTCAR中提取结构，并按着VASP-POSCAR格式保存

import linecache
import os

def locate_keywords_in_outcar(outcar_path):
    element_number = []
    element_name = []
    lattice_vector = []
    idx_atom_position = []

    # 通过定位“ions per type”获得原子数element_number，进而确定原子类型数n_element
    element_number_str = ""
    with open(outcar_path, 'r') as file_outcar:
        for lineno, line in enumerate(file_outcar, start=1):
            if "ions per type" in line:
                idx_element_number = lineno
                element_number_str = line
                break
    element_number_arr = element_number_str.split()
    element_number = [int(number) for number in element_number_arr[(element_number_arr.index("=") + 1):]]
    n_element = len(element_number)

    # 通过定位“POTCAR:”获得原子类型
    idx_element_name = 0
    with open(outcar_path, 'r') as file_outcar:
        for lineno, line in enumerate(file_outcar, start=1):
            if "POTCAR:" in line:
                idx_element_name = lineno
                break
    for i in range(n_element):
        line = linecache.getline(outcar_path, idx_element_name + i)
        element_name.append(line.split()[2])

    # 通过定位“direct lattice vectors”，获得晶格矢量
    idx_lattice_vector = 0
    with open(outcar_path, 'r') as file_outcar:
        for lineno, line in enumerate(file_outcar, start=1):
            if "direct lattice vectors" in line:
                idx_lattice_vector = lineno
                break
    for i in range(3):
        line = linecache.getline(outcar_path, idx_lattice_vector + i + 1)
        lattice_vector.append([float(v) for v in line.split()[:3]])

    # 通过定位“POSITION”和“TOTAL-FORCE”，获得原子坐标所在行
    with open(outcar_path, 'r') as file_outcar:
        idx_line = 0
        for line in file_outcar:
            idx_line += 1
            if "POSITION" in line and "TOTAL-FORCE" in line:
                idx_atom_position.append(idx_line)

    return element_name, element_number, lattice_vector, idx_atom_position

def output_poscar(outcar_path):

    dir_path = os.path.dirname(outcar_path)

    element_name, element_number, lat_vec, idx_atom_position = locate_keywords_in_outcar(outcar_path)
    output_str = "Automatically created by python \n1.0\n"
    for i in range(3):
        output_str += f"{lat_vec[i][0]:15.6f}{lat_vec[i][1]:15.6f}{lat_vec[i][2]:15.6f}\n"
    for element in element_name:
        output_str += f"{element}\t"
    output_str += "\n"
    for number in element_number:
        output_str += f"{number}\t"
    output_str += "\nCartesian\n"

    n_atom = sum(element_number)

    os.makedirs("vasp", exist_ok=True)

    for i, lineno in enumerate(idx_atom_position, start=1):
        output_vasp_file = os.path.join(dir_path, f"vasp/{i}.vasp")
        fout = open(output_vasp_file, "w")
        fout.write(output_str)
        for j in range(n_atom):
            line = linecache.getline(outcar_path, lineno + j + 2)
            pos = [float(p) for p in line.split()[:3]]
            fout.write(f"{pos[0]:15.6f}{pos[1]:15.6f}{pos[2]:15.6f}\n")
        fout.close()

output_poscar("OUTCAR")