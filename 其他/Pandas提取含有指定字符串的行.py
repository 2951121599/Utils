import pandas as pd

df = pd.read_csv('sample.csv').head(3)
print(df)
# 1.行的提取（选择）方法
mask = [True, False, True]
df_mask = df[mask]
# print(df_mask)

# 2.完全匹配==
# print(df[df['state'] == 'CA'])

# 3.部分匹配
# str.contains()：包含一个特定的字符串
# print(df[df['name'].str.contains('li')])


# 4.参数na：缺少值NaN处理
df_nan = df.copy()
df_nan.iloc[2, 0] = float('nan')
# 如果元素是缺失值NaN，则默认情况下它将返回NaN而不是True或False。
# print(df_nan['name'].str.contains('li'))
# 用作条件时，如果na = True，则选择NaN的行，如果na = False，则不选择NaN的行。
# print(df_nan[df_nan['name'].str.contains('li', na=True)])
# print(df_nan[df_nan['name'].str.contains('li', na=False)])
# print(df_nan[df_nan['name'].str.contains('Li', na=False, case=False)])  # case=False 不区分大小写


# 5.参数regex：使用正则表达式模式
# print(df['name'].str.contains('i.*e'))  # 默认情况下，指定为第一个参数的字符串将作为正则表达式模式进行处理。

df_q = df.copy()
df_q.iloc[2, 0] += '?'
# print(df_q)
# print(df_q['name'].str.contains('?', regex=False))
# print(df_q['name'].str.contains('\?'))  # 不用加regex=False


# 6.str.startswith（）：以特定的字符串开头
# print(df['name'].str.startswith('B'))
# print(df[df['name'].str.startswith('B')])

# 7.str.endswith（）：以特定字符串结尾
# print(df['name'].str.endswith('e'))
# print(df[df['name'].str.endswith('e')])


# 8.str.match（）：匹配正则表达式模式
# print(df['name'].str.match('.*i.*e'))  # 获取与正则表达式模式匹配
# print(df['name'].str.match('.*i'))  # 确定字符串的开头是否与模式匹配。如果不是一开始就为False。

