import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import squarify    # pip install squarify (algorithm for treemap)
import seaborn as sns


df = pd.read_excel('app_plans.xlsx')

df.drop(['Отметка времени'], axis = 'columns', inplace = True)
df.drop_duplicates(inplace = True)
print(df) 
print(df['Ваше имя и фамилия (по желанию)'])
df.drop(['Ваше имя и фамилия (по желанию)'], axis = 'columns', inplace=True)
#clearing the duplicate rows

df.columns = ['Основной ВУЗ', 'Запасной ВУЗ', 'Направление', 'Сколько обучались в ХЦ', 'По чему поступаете']
#renaming columns

df['Основной ВУЗ'] = df['Основной ВУЗ'].replace(['мфти'],'МФТИ')
df['Запасной ВУЗ'] = df['Запасной ВУЗ'].replace(['никакие','-'],np.NaN)
#replacing mistakes and misspellings


df_main_uni = df['Основной ВУЗ'].to_numpy()
df_main_uni = df_main_uni.tolist()
main_uni_help = [[x,df_main_uni.count(x)] for x in set(df_main_uni)]

help_arr = np.asarray(main_uni_help)

df_main_uni = pd.DataFrame(main_uni_help, columns=['ВУЗ', 'count'])
df_main_uni["count"] =df_main_uni['count'].astype('int')

squarify.plot(sizes=df_main_uni['count'], label=df_main_uni['ВУЗ'], alpha = 0.8)
plt.axis('off')
plt.show()




# arr = []
# for i in df['Основной вуз']:
    