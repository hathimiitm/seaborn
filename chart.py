
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Synthetic data generation
np.random.seed(42)
n = 500
email = np.random.lognormal(mean=3.5, sigma=0.6, size=n)
phone = np.random.lognormal(mean=2.5, sigma=0.5, size=n)
chat = np.random.lognormal(mean=2.0, sigma=0.4, size=n)
social = np.random.lognormal(mean=3.0, sigma=0.7, size=n)

df = pd.DataFrame({
    'ResponseTime': np.concatenate([email, phone, chat, social]),
    'Channel': ['Email']*n + ['Phone']*n + ['Chat']*n + ['Social']*n
})

sns.set_style("whitegrid")
sns.set_context("talk", font_scale=0.95)
plt.figure(figsize=(8,8))
palette = sns.color_palette("Set2")

ax = sns.violinplot(x='Channel', y='ResponseTime', data=df, palette=palette, inner='quartile', cut=0)
ax.set_title("Support Response Time Distribution by Channel", fontsize=16, weight='bold')
ax.set_ylabel("Response Time (minutes)", fontsize=12)
ax.set_xlabel("Support Channel", fontsize=12)
ax.set_yscale('log')
yticks = [1, 5, 10, 30, 60, 120, 300, 600, 1200]
ax.set_yticks(yticks)
ax.get_yaxis().set_major_formatter(matplotlib.ticker.FuncFormatter(lambda y, _: f'{int(y)}'))

plt.tight_layout()
plt.savefig('chart.png', dpi=64, bbox_inches='tight')
