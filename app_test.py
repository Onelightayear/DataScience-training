import pandas as pd 
import numpy as np
df = pd.read_excel('app_plans.xlsx')


df.drop(['Отметка времени', 'Ваше имя и фамилия (по желанию)'], axis = 'columns', inplace=True)

df.columns = ['Основной ВУЗ', 'Запасной ВУЗ', 'Направление', 'Сколько обучались в ХЦ', 'По чему поступаете']

df['Основной ВУЗ'] = df['Основной ВУЗ'].replace(['мфти'],'МФТИ')
df['Запасной ВУЗ'] = df['Запасной ВУЗ'].replace(['никакие','-'],np.NaN)
print(df.columns)
print(df['Запасной ВУЗ'])