import pandas as pd

df = pd.read_csv('sample.csv').head(3)
print(df)
# 1.�е���ȡ��ѡ�񣩷���
mask = [True, False, True]
df_mask = df[mask]
# print(df_mask)

# 2.��ȫƥ��==
# print(df[df['state'] == 'CA'])

# 3.����ƥ��
# str.contains()������һ���ض����ַ���
# print(df[df['name'].str.contains('li')])


# 4.����na��ȱ��ֵNaN����
df_nan = df.copy()
df_nan.iloc[2, 0] = float('nan')
# ���Ԫ����ȱʧֵNaN����Ĭ���������������NaN������True��False��
# print(df_nan['name'].str.contains('li'))
# ��������ʱ�����na = True����ѡ��NaN���У����na = False����ѡ��NaN���С�
# print(df_nan[df_nan['name'].str.contains('li', na=True)])
# print(df_nan[df_nan['name'].str.contains('li', na=False)])
# print(df_nan[df_nan['name'].str.contains('Li', na=False, case=False)])  # case=False �����ִ�Сд


# 5.����regex��ʹ��������ʽģʽ
# print(df['name'].str.contains('i.*e'))  # Ĭ������£�ָ��Ϊ��һ���������ַ�������Ϊ������ʽģʽ���д���

df_q = df.copy()
df_q.iloc[2, 0] += '?'
# print(df_q)
# print(df_q['name'].str.contains('?', regex=False))
# print(df_q['name'].str.contains('\?'))  # ���ü�regex=False


# 6.str.startswith���������ض����ַ�����ͷ
# print(df['name'].str.startswith('B'))
# print(df[df['name'].str.startswith('B')])

# 7.str.endswith���������ض��ַ�����β
# print(df['name'].str.endswith('e'))
# print(df[df['name'].str.endswith('e')])


# 8.str.match������ƥ��������ʽģʽ
# print(df['name'].str.match('.*i.*e'))  # ��ȡ��������ʽģʽƥ��
# print(df['name'].str.match('.*i'))  # ȷ���ַ����Ŀ�ͷ�Ƿ���ģʽƥ�䡣�������һ��ʼ��ΪFalse��

