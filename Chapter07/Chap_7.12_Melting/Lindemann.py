# ©️ Copyright 2023 @ Authors
# 作者：斯坦福大厨 📨
# 日期：2023-09-28
#  共享协议：本作品采用知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议进行许可。
# 恭喜您已经发现了这份神奇的计算材料学课件！这份课件是我在熬夜吃掉不计其数的披萨和咖啡后创作出来的，配套的教材是由单斌、陈征征、陈蓉合著的《计算材料学--从算法原理到代码实现》。
#学习资料合集您可以在这个网址找到：www.materialssimulation.com/book，您也可以跟着up主无人问津晦涩难懂的B站视频一起进行学习。希望它能帮您在计算材料学的道路上摔得不那么痛。
# 就像您尊重那些一边烘焙披萨一边写代码的大厨一样，当您使用这份课件时，请：
# 记得告诉大家这份课件是斯坦福大厨写的，并且他在华中科技大学微纳中心工作
# 别用它去赚大钱，这个课件是用来学习的，不是用来买披萨的
# 保持开放共享的精神
# 如果你有关于计算材料学的想法，或者你只是想和我讨论最好吃的披萨口味，欢迎通过邮件 bshan@mail.hust.edu.cn 联系我。

from ase import io
import numpy as np

def lindemann(filename, n_start=None, n_end=None):
    """
    Calculate the Lindemann index for atomic vibrations using the provided trajectory.

    Parameters:
    - filename: Name of the file containing atomic positions (typically a LAMMPS dump file).
    - n_start: Starting index for the trajectory.
    - n_end: Ending index for the trajectory.

    Returns:
    - Lindemann index value.
    """

    # Construct the slice string based on provided indices
    if n_start is None and n_end is None:
        slice_str = ":"
    elif n_start is None:
        slice_str = f":{n_end}"
    elif n_end is None:
        slice_str = f"{n_start}:"
    else:
        slice_str = f"{n_start}:{n_end}"

    # Read atomic positions from the file for the given range
    atoms = io.read(filename, slice_str, 'lammps-dump-text')

    # Total number of atoms and total number of timesteps
    N = atoms[0].positions.shape[0]
    N_t = len(atoms)
    print('number of atoms in each frame =',N, 'number of frames =',N_t)

    # Initialize arrays to store distances between atoms
    r_square = np.zeros((N_t, N, N))

    # Loop through each timestep
    for t in range(N_t):
        G = np.dot(atoms[t].positions, atoms[t].positions.T)
        H = np.tile(np.diag(G), (N, 1))

        # Compute the squared distance between each pair of atoms at time t
        r_square[t, :, :] = H + H.T - 2 * G

    # Compute average distance and squared average distance over all timesteps
    r_ave = np.mean(np.sqrt(r_square), axis=0)
    print(r_square.shape)
    print(r_ave.shape)
    print('r_ave_max =',np.max(r_ave), 'r_ave_min =',np.min(r_ave))

    r2_ave = np.mean(r_square, axis=0)
    print('r2_ave =',np.max(r2_ave))

    # Extract upper triangular part of matrices
    r_ave_upper = r_ave[np.triu_indices(N, k=1)]
    print('r_ave_upper_max =',np.max(r_ave_upper), 'r_ave_upper_min =',np.min(r_ave_upper))
    r2_ave_upper = r2_ave[np.triu_indices(N, k=1)]

    # Calculate Lindemann criterion for upper triangular elements
    value_upper = np.sqrt(r2_ave_upper - np.power(r_ave_upper, 2)) / r_ave_upper

    # Sum over all unique atom pairs
    total_value = np.sum(value_upper)

    # Normalize by the total number of atom pairs
    return total_value * 2 / (N * (N - 1))

if __name__ == '__main__':
    lindemann_values = []
    data = lindemann('lammps_dump.atom')
    print(f'Lindemann index ={data}')