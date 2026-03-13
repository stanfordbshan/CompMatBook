<div align="center">

# 《计算材料学 -- 从算法原理到代码实现》

**单斌 &nbsp; 陈征征 &nbsp; 陈蓉 &nbsp; 编著**

**华中科技大学出版社 &nbsp; 2023**

<img src="https://github.com/stanfordbshan/CompMatBook/blob/main/cover.png?raw=true" width="280"/>

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](LICENSE)
![Language](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)
![VASP](https://img.shields.io/badge/Software-VASP-green)
![LAMMPS](https://img.shields.io/badge/Software-LAMMPS-orange)

</div>

---

本仓库为教材《计算材料学——从算法原理到代码实现》的配套代码与算例资源，涵盖第一性原理计算、分子动力学、蒙特卡罗方法等计算材料学核心方法的算法实现与实例演示。

## 快速导航

| 章节 | 主题 | 代码 |
|:---:|:---|:---:|
| 前置 | Python 与科学计算基础 | [Prerequisite](Prerequisite/) |
| 第一章 | 数学基础 | [Chapter01](Chapter01/) |
| 第三章 | 第一性原理的微观计算模拟 | [Chapter03](Chapter03/) |
| 第四章 | VASP 计算模拟实例 | [Chapter04](Chapter04/) |
| 第六章 | 分子动力学方法 | [Chapter06](Chapter06/) |
| 第七章 | LAMMPS 分子动力学实例 | [Chapter07](Chapter07/) |
| 第八章 | 蒙特卡罗方法 | [Chapter08](Chapter08/) |

---

## 目录

<details>
<summary><b>前置：Python 与科学计算基础</b></summary>

- Python 与科学计算（上）
- Python 与科学计算（下）
- 用 Python 探索分形几何

</details>

<details>
<summary><b>第一章 &nbsp; 数学基础</b></summary>

- **1.1** 矩阵运算
  - 1.1.1 行列式 &ensp;|&ensp; 1.1.2 矩阵的本征值问题 &ensp;|&ensp; 1.1.3 矩阵分解 &ensp;|&ensp; 1.1.4 幺正变换
- **1.2** 群论基础
  - 1.2.1 群的定义 &ensp;|&ensp; 1.2.2 子群、陪集、正规子群与商群 &ensp;|&ensp; 1.2.3 直积群 &ensp;|&ensp; 1.2.4 群的矩阵表示 &ensp;|&ensp; 1.2.5 三维转动反演群 O(3)
- **1.3** 最优化方法
  - 1.3.1 最速下降法 &ensp;|&ensp; 1.3.2 共轭梯度法 &ensp;|&ensp; 1.3.3 牛顿法与拟牛顿法 &ensp;|&ensp; 1.3.4 一维搜索 &ensp;|&ensp; 1.3.5 单纯形法 &ensp;|&ensp; 1.3.6 最小二乘法 &ensp;|&ensp; 1.3.7 拉格朗日乘子
- **1.4** 矢量正交化
  - 1.4.1 施密特正交化 &ensp;|&ensp; 1.4.2 正交多项式
- **1.5** 积分方法
  - 1.5.1 矩形积分法 &ensp;|&ensp; 1.5.2 梯形积分法 &ensp;|&ensp; 1.5.3 辛普森积分法 &ensp;|&ensp; 1.5.4 高斯积分法 &ensp;|&ensp; 1.5.5 蒙特卡罗积分方法

</details>

<details>
<summary><b>第二章 &nbsp; 量子力学和固体物理基础</b></summary>

- **2.1** 量子力学
  - 2.1.1 量子力学简介 &ensp;|&ensp; 2.1.2 薛定谔方程 &ensp;|&ensp; 2.1.3 波函数的几率诠释 &ensp;|&ensp; 2.1.4 力学量算符和表象变换 &ensp;|&ensp; 2.1.5 一维方势阱 &ensp;|&ensp; 2.1.6 方势垒的隧穿 &ensp;|&ensp; 2.1.7 WKB 方法 &ensp;|&ensp; 2.1.8 传递矩阵法 &ensp;|&ensp; 2.1.9 氢原子 &ensp;|&ensp; 2.1.10 变分法
- **2.2** 晶体对称性
  - 2.2.1 晶体结构和点群 &ensp;|&ensp; 2.2.2 常见晶体结构和晶面 &ensp;|&ensp; 2.2.3 结构缺陷
- **2.3** 晶体的力学性质
  - 2.3.1 状态方程 &ensp;|&ensp; 2.3.2 应变与应力 &ensp;|&ensp; 2.3.3 弹性常数
- **2.4** 固体能带论
  - 2.4.1 周期边界、倒空间与 Bloch 定理 &ensp;|&ensp; 2.4.2 空晶格模型与第一布里渊区 &ensp;|&ensp; 2.4.3 近自由电子近似与能带间隙 &ensp;|&ensp; 2.4.4 晶体能带结构 &ensp;|&ensp; 2.4.5 介电函数
- **2.5** 晶格振动与声子谱

</details>

<details>
<summary><b>第三章 &nbsp; 第一性原理的微观计算模拟</b></summary>

- **3.1** 分子轨道理论
  - 3.1.1 波恩-奥本海默近似 &ensp;|&ensp; 3.1.2 平均场的概念 &ensp;|&ensp; 3.1.3 电子的空间轨道与自旋轨道 &ensp;|&ensp; 3.1.4 Hartree-Fock 方法 &ensp;|&ensp; 3.1.5 HF 近似下的单电子自洽方程 &ensp;|&ensp; 3.1.6 Hartree-Fock 单电子波函数的讨论 &ensp;|&ensp; 3.1.7 闭壳层体系中的 HF 方程 &ensp;|&ensp; 3.1.8 开壳层体系中的 HF 方程 &ensp;|&ensp; 3.1.9 HF 方程的矩阵表达 &ensp;|&ensp; 3.1.10 Koopmans 定理 &ensp;|&ensp; 3.1.11 均匀电子气模型 &ensp;|&ensp; 3.1.12 HF 方程的数值求解和基组选取 &ensp;|&ensp; 3.1.13 X&alpha; 方法和超越 HF 近似
- **3.2** 密度泛函理论
  - 3.2.1 托马斯-费米-狄拉克近似 &ensp;|&ensp; 3.2.2 Hohenberg-Kohn 定理 &ensp;|&ensp; 3.2.3 Kohn-Sham 方程 &ensp;|&ensp; 3.2.4 交换关联能概述 &ensp;|&ensp; 3.2.5 局域密度近似 &ensp;|&ensp; 3.2.6 广义梯度近似 &ensp;|&ensp; 3.2.7 混合泛函 &ensp;|&ensp; 3.2.8 强关联与 LDA+U 方法
- **3.3** 赝势
  - 3.3.1 正交化平面波 &ensp;|&ensp; 3.3.2 模守恒赝势 &ensp;|&ensp; 3.3.3 赝势的分部形式 &ensp;|&ensp; 3.3.4 超软赝势
- **3.4** 平面波赝势方法
  - 3.4.1 布里渊区积分——特殊 k 点 &ensp;|&ensp; 3.4.2 布里渊区积分——四面体法 &ensp;|&ensp; 3.4.3 平面波-赝势框架下体系的总能 &ensp;|&ensp; 3.4.4 自洽场计算的实现 &ensp;|&ensp; 3.4.5 利用共轭梯度法求解广义本征值 &ensp;|&ensp; 3.4.6 迭代对角化方法 &ensp;|&ensp; 3.4.7 Hellmann-Feynman 力
- **3.5** 缀加平面波 (APW) 方法及其线性化
  - 3.5.1 APW 方法的理论基础及公式推导 &ensp;|&ensp; 3.5.2 APW 方法的线性化处理 &ensp;|&ensp; 3.5.3 关于势函数的讨论
- **3.6** 过渡态
  - 3.6.1 拖曳法与 NEB 方法 &ensp;|&ensp; 3.6.2 Dimer 方法
- **3.7** 电子激发谱与准粒子近似
  - 3.7.1 基本图像 &ensp;|&ensp; 3.7.2 格林函数理论与 Dyson 方程 &ensp;|&ensp; 3.7.3 GW 方法 &ensp;|&ensp; 3.7.4 Bethe-Salpeter 方程
- **3.8** 应用实例
  - 3.8.1 缺陷形成能 &ensp;|&ensp; 3.8.2 表面能 &ensp;|&ensp; 3.8.3 表面巨势 &ensp;|&ensp; 3.8.4 集团展开与二元合金相图

</details>

<details>
<summary><b>第四章 &nbsp; VASP 计算模拟实例</b></summary>

- **4.1** VASP 程序介绍
- **4.2** 辅助建模软件 Atomsk
- **4.3** 后处理程序 VASPKIT
- **4.4** 小分子气体能量计算
- **4.5** C&#8322;H&#8325;OH 的振动模式与频率计算
- **4.6** 材料平衡晶格常数计算
- **4.7** 堆垛层错能的计算
- **4.8** 多元合金的弹性性能计算
- **4.9** 空位形成能和间隙能计算
- **4.10** 晶体 Si 的能带结构计算
- **4.11** 基于 HSE06 的态密度与能带计算
- **4.12** 表面能的计算
- **4.13** 缺陷石墨烯的 STM 图像计算模拟
- **4.14** Pt 表面简单物种的吸附能计算
- **4.15** Pt(111) 表面羟基解离的过渡态搜索
- **4.16** Pt 表面的 ORR 催化路径

</details>

<details>
<summary><b>第五章 &nbsp; 紧束缚方法</b></summary>

- **5.1** 建立 Hamiltonian 矩阵
  - 5.1.1 双原子分子 &ensp;|&ensp; 5.1.2 原子轨道线性组合方法 &ensp;|&ensp; 5.1.3 Slater-Koster 双中心近似 &ensp;|&ensp; 5.1.4 哈密顿矩阵元的普遍表达式 &ensp;|&ensp; 5.1.5 对自旋极化的处理 &ensp;|&ensp; 5.1.6 光吸收谱
- **5.2** 体系总能与计算原子受力
- **5.3** 自洽紧束缚方法
  - 5.3.1 Harris-Foulkes 非自洽泛函 &ensp;|&ensp; 5.3.2 电荷自洽紧束缚方法
- **5.4** 应用实例
  - 5.4.1 闪锌矿的能带结构 &ensp;|&ensp; 5.4.2 石墨烯和碳纳米管的能带结构

</details>

<details>
<summary><b>第六章 &nbsp; 分子动力学方法</b></summary>

- **6.1** 简介
  - 6.1.1 分子动力学基本步骤 &ensp;|&ensp; 6.1.2 系综平均与时间平均 &ensp;|&ensp; 6.1.3 周期性边界条件 &ensp;|&ensp; 6.1.4 近邻列表算法
- **6.2** 原子间相互作用势
  - 6.2.1 对势 &ensp;|&ensp; 6.2.2 晶格反演势 &ensp;|&ensp; 6.2.3 嵌入原子势 (EAM) &ensp;|&ensp; 6.2.4 改良型嵌入原子势 (MEAM) &ensp;|&ensp; 6.2.5 机器学习势
- **6.3** 微正则系综分子动力学
  - 6.3.1 前向欧拉算法 &ensp;|&ensp; 6.3.2 Verlet 算法 &ensp;|&ensp; 6.3.3 速度 Verlet 算法 &ensp;|&ensp; 6.3.4 蛙跳算法 &ensp;|&ensp; 6.3.5 预测-校正算法
- **6.4** 正则系综
  - 6.4.1 热浴和正则系综 &ensp;|&ensp; 6.4.2 NPT 系综
- **6.5** 第一原理分子动力学
  - 6.5.1 波恩-奥本海默分子动力学 &ensp;|&ensp; 6.5.2 Car-Parrinello 分子动力学
- **6.6** 分子动力学的应用

</details>

<details>
<summary><b>第七章 &nbsp; LAMMPS 分子动力学实例</b></summary>

- **7.1** LAMMPS 程序介绍
- **7.2** 可视化程序 OVITO
- **7.3** 惰性气体的扩散运动与平衡速率分布
- **7.4** 气体分子的布朗运动
- **7.5** 大质量粒子的二维布朗运动
- **7.6** 材料的热膨胀系数计算
- **7.7** 体积热容的计算
- **7.8** Cu 的声子谱计算
- **7.9** Ni 裂纹扩展机理计算
- **7.10** LiS 锂硫电池体积膨胀的模拟
- **7.11** 体相 Pt 的熔点与径向分布函数计算
- **7.12** Pt 纳米颗粒的熔点与表面熔化
- **7.13** Pt 纳米颗粒的烧结
- **7.14** 氢原子在 BCC-铁中的扩散
- **7.15** Ni 纳米线的屈服机制
- **7.16** SiGe 纳米线的热导率计算
- **7.17** 多晶四元合金的切削分子动力学模拟
- **7.18** Si 表面的薄膜沉积
- **7.19** Hybrid 势模拟石墨烯对金属纳米线的卷绕过程

</details>

<details>
<summary><b>第八章 &nbsp; 蒙特卡罗方法</b></summary>

- **8.1** 蒙特卡罗方法基本原理
- **8.2** 计算函数积分与采样策略
  - 8.2.1 简单采样 &ensp;|&ensp; 8.2.2 重要性采样 &ensp;|&ensp; 8.2.3 Metropolis 采样
- **8.3** 几种重要的算法与模型
  - 8.3.1 NVT 正则系综的 MC 算法 &ensp;|&ensp; 8.3.2 NPT 正则系综的 MC 算法 &ensp;|&ensp; 8.3.3 巨正则系综的 MC 算法 &ensp;|&ensp; 8.3.4 Ising 模型 &ensp;|&ensp; 8.3.5 格子气模型 &ensp;|&ensp; 8.3.6 Potts 模型 &ensp;|&ensp; 8.3.7 XY 模型
- **8.4** Gibbs 系综
  - 8.4.1 随机事件及其接受几率 &ensp;|&ensp; 8.4.2 GEMC 算法实现
- **8.5** 统计力学中的应用
  - 8.5.1 随机行走 &ensp;|&ensp; 8.5.2 利用 Ising 模型观察铁磁-顺磁相变 &ensp;|&ensp; 8.5.3 逾渗问题
- **8.6** 动力学蒙特卡罗方法 (KMC)
  - 8.6.1 KMC 方法的基本原理 &ensp;|&ensp; 8.6.2 指数分布与 KMC 方法的时间步长 &ensp;|&ensp; 8.6.3 计算跃迁速率 &ensp;|&ensp; 8.6.4 KMC 几种不同的实现算法 &ensp;|&ensp; 8.6.5 低势垒问题与小概率事件 &ensp;|&ensp; 8.6.6 实体动力学蒙特卡洛方法 &ensp;|&ensp; 8.6.7 KMC 的若干进展
- **8.7** KMC 的应用
  - 8.7.1 表面迁移 &ensp;|&ensp; 8.7.2 晶体生长 &ensp;|&ensp; 8.7.3 模拟程序升温脱附过程

</details>

<details>
<summary><b>第九章 &nbsp; 附录</b></summary>

- **9.1** 角动量算符在球坐标中的表达式
- **9.2** 拉普拉斯算符在球坐标中的表达式
- **9.3** 勒让德多项式、球谐函数与角动量耦合
- **9.4** 三次样条
- **9.5** 傅里叶变换
  - 9.5.1 基本概念 &ensp;|&ensp; 9.5.2 离散傅里叶变换 &ensp;|&ensp; 9.5.3 快速傅里叶变换
- **9.6** 结构分析
  - 9.6.1 辨别 BCC、FCC 以及 HCP 结构 &ensp;|&ensp; 9.6.2 中心对称参数 &ensp;|&ensp; 9.6.3 Voronoi 算法构造多晶体系
- **9.7** NEB 常用的优化算法
  - 9.7.1 Quick-Min 算法 &ensp;|&ensp; 9.7.2 FIRE 算法
- **9.8** Pulay 电荷更新
- **9.9** 最近邻原子的确定

</details>

---

## 环境与工具

| 工具 | 用途 |
|:---|:---|
| **Python / Jupyter** | 算法原理演示与数值实现 |
| **VASP** | 第一性原理电子结构计算 (第四章) |
| **LAMMPS** | 经典分子动力学模拟 (第七章) |
| **OVITO** | 分子动力学可视化后处理 |
| **VASPKIT / Atomsk / ASE** | 建模与后处理辅助工具 |

## 许可证

本项目采用 [GPL-3.0](LICENSE) 许可证。

<div align="center">

<img src="https://github.com/stanfordbshan/CompMatBook/blob/main/author.png?raw=true" width="500"/>

</div>
