import pandas as pd

df = pd.read_csv("data/jobs.csv")

print(df)
print()
print("Total jobs:", len(df))