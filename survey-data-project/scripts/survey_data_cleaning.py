import pandas as pd

# Load raw data
df = pd.read_csv("data/survey_raw_data.csv")

# Step 1: Basic cleaning
df.drop_duplicates(inplace=True)
df_cleaned = df.dropna(subset=["Age", "Gender"])
df_cleaned["Satisfaction_with_Service"].fillna(df_cleaned["Satisfaction_with_Service"].median(), inplace=True)
df_cleaned["Recommend_to_Others"].fillna("No Response", inplace=True)
df_cleaned["Comments"].fillna("", inplace=True)

# Save cleaned data
df_cleaned.to_csv("outputs/survey_cleaned_data.csv", index=False)
print("Cleaned data saved as 'outputs/survey_cleaned_data.csv'")
