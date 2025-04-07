import pandas as pd

# Load cleaned data
df = pd.read_csv("outputs/survey_cleaned_data.csv")

# Step 2: Data manipulation and summary reporting
report = {}

# Average satisfaction
total_avg = df["Satisfaction_with_Service"].mean()
report["Average_Satisfaction"] = round(total_avg, 2)

# Recommendation breakdown
recommend_counts = df["Recommend_to_Others"].value_counts().to_dict()
report["Recommend_Breakdown"] = recommend_counts

# Satisfaction by Gender
satisfaction_by_gender = df.groupby("Gender")["Satisfaction_with_Service"].mean().round(2).to_dict()
report["Satisfaction_by_Gender"] = satisfaction_by_gender

# Save report to Excel
with pd.ExcelWriter("outputs/survey_report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Cleaned Data", index=False)
    pd.DataFrame.from_dict(report, orient="index").to_excel(writer, sheet_name="Summary Report")

print("Report saved as 'outputs/survey_report.xlsx'")
