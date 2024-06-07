import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from scipy.stats import wilcoxon, ttest_1samp
import pandas as pd

# 读取excel文件
file_path = '插层前后差值.xlsx'
df = pd.read_excel(file_path)

# 设置matplotlib中文字体支持中文显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


# 定义函数用于执行检验并打印结果
def perform_test_and_print(column_data, test_name, test_func):
    _, p_val = test_func(column_data)
    result = "拒绝原假设: 数据不符合正态分布条件。" if p_val < 0.05 else "未能拒绝原假设: 数据符合正态分布条件。"
    print(f"{test_name}: p-value = {p_val}, {result}")


# 遍历除最后一列外的所有列
for col in df.columns[:-1]:
    sample_data = df[col]
    statistic, p_value = stats.shapiro(sample_data)

    print(f"Column: {col}")
    print(f"Statistic: {statistic}, p-value: {p_value}")

    # 数据可视化
    plt.figure(figsize=(10, 6))
    sns.histplot(sample_data, bins=20, color="skyblue", kde=True, stat='density', kde_kws={'bw_adjust': 0.5})

    mu = sample_data.mean()
    sigma = sample_data.std()
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = stats.norm.pdf(x, mu, sigma)
    plt.plot(x, p, 'r', linewidth=2, label=f'Fit: μ={mu:.2f}, σ={sigma:.2f}')

    plt.title(f'{col} 数据分布与正态分布拟合')
    plt.xlabel('值')
    plt.ylabel('密度')
    plt.legend()

    alpha = 0.05
    if p_value < alpha:
        print("拒绝原假设: 数据不遵循正态分布。")
        # 对非正态分布数据进行 Wilcoxon 符号秩检验
        perform_test_and_print(sample_data, "Wilcoxon 符号秩检验", wilcoxon)
    else:
        print("未能拒绝原假设: 数据视觉上遵循正态分布。")
        # 对正态分布数据进行 T 检验 (这里以单样本T检验为例，假设检验数据是否与0有显著差异)
        perform_test_and_print(sample_data, "T 检验", lambda x: ttest_1samp(x, popmean=0))

    plt.show()
    plt.close()

print("所有列的正态性检验、Wilcoxon 符号秩检验及T检验已完成。")