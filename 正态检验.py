import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import pandas as pd

# 文件路径
file_path = '插层前后差值.xlsx'

# 读取Excel文件到DataFrame
df = pd.read_excel(file_path)

# 设置matplotlib中文字体支持中文显示（如果需要的话）
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用黑体显示中文
plt.rcParams['axes.unicode_minus'] = False  # 正常显示负号

# 遍历除最后一列外的所有列
for col in df.columns[:-1]:
    # 提取当前列数据
    sample_data = df[col]

    # 进行正态性检验
    statistic, p_value = stats.shapiro(sample_data)

    # 输出统计量和p值
    print(f"Column: {col}")
    print(f"Statistic: {statistic}, p-value: {p_value}")

    # 数据可视化
    plt.figure(figsize=(10, 6))

    # 绘制样本数据的直方图
    sns.histplot(sample_data, bins=20, color="skyblue", kde=True, stat='density', kde_kws={'bw_adjust': 0.5})

    # 计算正态分布的理论曲线参数
    mu = sample_data.mean()  # 样本均值
    sigma = sample_data.std()  # 样本标准差
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, sigma)  # 正态分布概率密度函数

    # 叠加正态分布曲线
    plt.plot(x, p, 'r', linewidth=2, label=f'Fit: μ={mu:.2f}, σ={sigma:.2f}')

    # 图形美化和标签
    plt.title(f'{col} 数据分布与正态分布拟合')
    plt.xlabel('值')
    plt.ylabel('密度')
    plt.legend()

    # 基于p值判断是否拒绝原假设
    alpha = 0.05
    if p_value < alpha:
        print("拒绝原假设: 数据不遵循正态分布。")
    else:
        print("未能拒绝原假设: 数据视觉上遵循正态分布。")

    # 显示图形并保存到文件，避免立即显示以方便批量处理
    # 如果需要即时查看图形，取消下面这行的注释
    plt.show()
    plt.close()  # 关闭当前图形以免内存泄漏

print("所有列的正态性检验及可视化已完成。")