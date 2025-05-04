from seaborn import scatterplot
from sklearn.datasets import load_breast_cancer
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = load_breast_cancer()
df = pd.DataFrame(data.data, columns=data.feature_names)
# Добавляем целевую переменную (классы) в таблицу
df['target'] = data.target
#print(df.head())
#print(data.DESCR)
#print(df[['mean radius', 'mean texture', 'target']].describe())

sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))
sc = sns.scatterplot(
    x='mean radius',
    y='mean texture',
    hue='target',
    hue_order = [0, 1],
    data=df,
    palette={0: 'red', 1: 'green'},
    alpha=0.7  # Прозрачность маркеров
)
plt.xlabel('Mean Radius, cm')
plt.ylabel('Mean Texture')
plt.title(' Mean Radius vs Mean Texture')
# Получаем текущие элементы легенды
handles, _ = sc.get_legend_handles_labels()
labels = ['Malignant (0)', 'Benign (1)']
plt.legend(
    handles=handles,
    labels=labels,
    title='Class'
)
plt.show()
print(df['target'].dtype)