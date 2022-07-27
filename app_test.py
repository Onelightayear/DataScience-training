import pandas as pd 
import numpy as np
df = pd.read_excel('app_plans.xlsx')

print(df['Ваше имя и фамилия (по желанию)'])
df.drop_duplicates(subset=['Ваше имя и фамилия (по желанию)'])
print(df) 

df.drop(['Отметка времени', 'Ваше имя и фамилия (по желанию)'], axis = 'columns', inplace=True)

df.columns = ['Основной ВУЗ', 'Запасной ВУЗ', 'Направление', 'Сколько обучались в ХЦ', 'По чему поступаете']

df['Основной ВУЗ'] = df['Основной ВУЗ'].replace(['мфти'],'МФТИ')
df['Запасной ВУЗ'] = df['Запасной ВУЗ'].replace(['никакие','-'],np.NaN)



# for i in df['По чему поступаете', i]:
#     x = df['По чему поступаете', i]
#     arr = x.split(', ')
#     if arr[1].find('По перечневым') != -1:
#         del arr[1]
#         new_str = ', '.join([str(elem) for elem in s])
#         df['По чему поступаете'] = df['По чему поступаете'].replace([x],new_str)
sub_df = df['Основной ВУЗ']
# print(sub_df)
sub_df.plot(kind = 'pie', subplots = True, figsize=(8,8))
plt.show()