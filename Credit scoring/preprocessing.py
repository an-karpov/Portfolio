from typing import List

import numpy as np
import pandas as pd

DATASET_PATH = "https://raw.githubusercontent.com/evgpat/edu_stepik_from_idea_to_mvp/main/datasets/credit_scoring.csv"
SAVE_PATH = "./data/"

def drop_outliers(df: pd.DataFrame, columns:List[str]) -> pd.DataFrame:
    "drop outliers from df"
    quantiles = df[columns+['GroupAge']].groupby(by="GroupAge").quantile(q=0.95)

    def is_not_outlier(s):
        res = True
        for col in columns:
            res = res and (s[col] <= quantiles.loc[s.GroupAge][col])
        return res

    return df[df.apply(is_not_outlier, axis=1)]

# import data
print("Importing data...")
df = pd.read_csv(DATASET_PATH)
df_shape = df.shape[0]
print("Done...")

print("Preprocessing...")
# fill NaNs
df["MonthlyIncome"] = df[["MonthlyIncome", "GroupAge"]].groupby("GroupAge").transform(lambda x: x.fillna(x.median()))

dependents_mode = df["NumberOfDependents"].mode()[0]
df["NumberOfDependents"] = df["NumberOfDependents"].fillna(dependents_mode)

age_e_median = df[df["GroupAge"]=='e']["age"].median()
df["age"] = df["age"].fillna(age_e_median)

# drop outliers
columns_with_outliers = ["RevolvingUtilizationOfUnsecuredLines", "DebtRatio", "MonthlyIncome"]
df = drop_outliers(df, columns_with_outliers)
df = df.loc[df["NumberOfTimes90DaysLate"] <= 17]

print("Done...")
print("Before: ", df_shape)
print("After: ", df.shape[0])

# Save data
print("Saving data...")
df.to_csv(SAVE_PATH + "preprocessed_data.csv", index=False)
