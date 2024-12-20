import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
path = "C:/Users/HP/PycharmProjects/PhD6/data/scopus.csv"
data = pd.read_csv(path)

# Calculate publication trend
publication_trend = data['Year'].value_counts().sort_index()

# Calculate citation trend
citation_trend = data.groupby('Year')['Cited by'].sum()

# Create subplots
fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Plot publication trend
axs[0].bar(publication_trend.index,
           publication_trend.values, color='skyblue')
axs[0].set_title('Publication Trend Over Years', fontsize=16)
axs[0].set_xlabel('Year', fontsize=14)
axs[0].set_ylabel('Number of Publications', fontsize=14)
axs[0].grid(axis='y', linestyle='--', alpha=0.7)

# Annotate publication trend
for i, v in enumerate(publication_trend.values):
    axs[0].text(publication_trend.index[i],
                v + 0.5, str(v), ha='center', fontsize=10)

# Plot citation trend
axs[1].plot(citation_trend.index,
            citation_trend.values, marker='o', color='orange')
axs[1].set_title('Citation Trend Over Years', fontsize=16)
axs[1].set_xlabel('Year', fontsize=14)
axs[1].set_ylabel('Total Citations', fontsize=14)
axs[1].grid()

# Annotate citation trend
for i, v in enumerate(citation_trend.values):
    axs[1].text(citation_trend.index[i],
                v + 5, str(v), ha='center', fontsize=10)

# Set overall title
# fig.suptitle('Publication and Citation Trends', fontsize=18)

# Adjust layout
plt.tight_layout(rect=(0, 0.03, 1, 0.95))
plt.show()

