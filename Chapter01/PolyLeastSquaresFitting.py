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

import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"]=["SimHei"] #设置字体
plt.rcParams["axes.unicode_minus"]=False #该语句解决图像中的“-”负号的乱码问题

num_data = 10
np.random.seed(7)
x = -1.0 + 2 * np.random.rand(num_data)
p0_true = -0.5
p1_true = 1.0
p2_true = 2.0
p3_true = 3.0
noise_level = 1.5
y = p0_true + p1_true*x + p2_true*x**2 + p3_true*x**3+ noise_level*np.random.randn(num_data)

#继续用一阶线性拟合结果
J = np.hstack([np.ones((num_data, 1)), x.reshape((num_data, 1))])
p, _, _, _ = np.linalg.lstsq(J, y, rcond=None)
print(f'Linear : p_0 = {p[0]:.{2}}, p_1 = {p[1]:.{2}}')

#用三阶多项式拟合结果
J = np.hstack([np.ones((num_data, 1)), x.reshape((num_data, 1)), x.reshape((num_data, 1)) ** 2,x.reshape((num_data, 1)) ** 3])
p_poly, _, _, _ = np.linalg.lstsq(J, y, rcond=None)
print(f'Polynomial : p_0 = {p_poly[0]:.2f}, p_1 = {p_poly[1]:.2f}')
print(f'        p_2 = {p_poly[2]:.2f}, p_3 = {p_poly[3]:.2f}')

#数据可视化
fig, ax = plt.subplots(dpi=300)
xx = np.linspace(-1, 1, 20)
yy_true = p0_true + p1_true * xx + p2_true*xx**2 +p3_true*xx**3
#一阶线性结果
yy = p[0] + p[1] * xx
#多项式结果
yy_poly = p_poly[0] + p_poly[1] * xx + p_poly[2]*xx**2 + p_poly[3]*xx**3
#叠加作图
ax.plot(x, y, 'x', color='k',ms=6,mew=2,label='有噪点的数据')
ax.plot(xx, yy_true, color='k',label='理论关系曲线')
ax.plot(xx, yy, '--', color='b',label='一阶线性模型')
ax.plot(xx, yy_poly, '-.', color='b',label='三阶多项式模型')
plt.legend(loc='best');
plt.show()