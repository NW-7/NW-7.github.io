import statsmodels.api as sm
import pandas as pd
import matplotlib.pyplot as plt

data = sm.datasets.copper.load_pandas()
df = data.data
#print( df.columns.tolist())
#print(df.head())
df = df.assign(YEAR = df.TIME + 1950)
#print(df.head())
filtered_df = df[(df['YEAR'] >= 1961) & (df['YEAR'] <= 1970)]
# Проверка
#print(filtered_df[['YEAR', 'WORLDCONSUMPTION', 'COPPERPRICE', 'ALUMPRICE']])

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(12, 10))

# --- График 1: Мировое потребление меди ---
ax1.plot(
    filtered_df['YEAR'],
    filtered_df['WORLDCONSUMPTION'],
    label='Мировое потребление (тыс. тонн)',
    color='blue',
    marker='o',
    linestyle='-'
)

# Настройки для первого графика
ax1.set_title('Динамика мирового потребления меди (1961–1970)', fontsize=14)
ax1.set_xlabel('Год', fontsize=12)
ax1.set_ylabel('Потребление, тыс. тонн', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.legend()
ax1.set_xticks(filtered_df['YEAR'])

# --- График 2: Цены на медь и алюминий ---
ax2.plot(
    filtered_df['YEAR'],
    filtered_df['COPPERPRICE'],
    label='Цена на медь ($/тонн)',
    color='green',
    marker='s',
    linestyle='--'
)

ax2.plot(
    filtered_df['YEAR'],
    filtered_df['ALUMPRICE'],
    label='Цена на алюминий ($/тонн)',
    color='red',
    marker='^',
    linestyle='-.'
)

# Настройки для второго графика
ax2.set_title('Динамика цен на медь и алюминий (1961–1970)', fontsize=14)
ax2.set_xlabel('Год', fontsize=12)
ax2.set_ylabel('Цена, $/тонн', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.legend()
ax2.set_xticks(filtered_df['YEAR'])

plt.tight_layout()
plt.show()
