import pandas as pd

url = "https://raw.githubusercontent.com/vikashishere/Datasets/refs/heads/main/data.csv"
df = pd.read_csv(url)
print("DataFrame loaded. Here's a preview:")
print(df.head())
df.to_csv("data.csv", index=False)
