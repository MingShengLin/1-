import pandas as pd

# 读取Excel文件
df = pd.read_excel('data2.xlsx')

# 定义最小-最大规范化函数
def min_max_normalization(df, columns):
    for column in columns:
        df[column] = (df[column] - df[column].min()) / (df[column].max() - df[column].min())
    return df

# 指定需要规范化的列名，排除非数值列如'组别'
columns_to_normalize = df.columns[1:]

# 应用最小-最大规范化
df_normalized = min_max_normalization(df, columns_to_normalize)

# 输出到新的Excel文件
df_normalized.to_excel('normalized_data.xlsx', index=False)

print("数据最小-最大规范化处理完成，已保存至normalized_data.xlsx")