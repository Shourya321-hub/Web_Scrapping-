import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("output/quotes_cleaned.csv")

print("=" * 50)
print("EXPLORATORY DATA ANALYSIS")
print("=" * 50)

# Basic information
print("\nDataset shape:")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nFirst 5 records:")
print(df.head())

# ---------------------------------------
# 1. Quotes by Author
# ---------------------------------------

author_counts = df["Author"].value_counts().head(10)

print("\nTop 10 Authors:")
print(author_counts)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=author_counts.values,
    y=author_counts.index
)

plt.title("Top 10 Authors by Number of Quotes")
plt.xlabel("Number of Quotes")
plt.ylabel("Author")

plt.tight_layout()

plt.savefig("output/top_authors.png")

plt.show()

# ---------------------------------------
# 2. Process Tags
# ---------------------------------------

all_tags = []

for tags in df["Tags"]:

    if pd.notna(tags) and tags.strip():

        tag_list = tags.split(",")

        for tag in tag_list:
            all_tags.append(tag.strip())

tag_counts = pd.Series(all_tags).value_counts().head(10)

print("\nTop 10 Tags:")
print(tag_counts)

plt.figure(figsize=(10, 6))

sns.barplot(
    x=tag_counts.values,
    y=tag_counts.index
)

plt.title("Top 10 Most Common Tags")
plt.xlabel("Frequency")
plt.ylabel("Tag")

plt.tight_layout()

plt.savefig("output/top_tags.png")

plt.show()

# ---------------------------------------
# 3. Number of Unique Authors
# ---------------------------------------

unique_authors = df["Author"].nunique()

print("\nNumber of unique authors:", unique_authors)

# ---------------------------------------
# 4. Number of Quotes
# ---------------------------------------

print("Total number of quotes:", len(df))

# ---------------------------------------
# 5. Average Tags per Quote
# ---------------------------------------

df["Tag_Count"] = df["Tags"].apply(
    lambda x: len(x.split(",")) if x else 0
)

print(
    "Average tags per quote:",
    round(df["Tag_Count"].mean(), 2)
)

# ---------------------------------------
# Final message
# ---------------------------------------

print("\nEDA completed successfully.")
print("Charts saved inside the output folder.")
