# Survey Data Processing & Reporting Automation

## Overview
This project simulates a real-world data processing workflow for survey data. It mirrors tasks in entry-level data analyst roles, focusing on:
- Data cleaning
- Variable manipulation
- Summary report generation
- Automation using Python and Excel

## Project Structure
```
survey-data-project/
├── data/
│   └── survey_raw_data.csv
├── outputs/
│   └── survey_cleaned_data.csv (generated)
│   └── survey_report.xlsx (generated)
├── scripts/
│   ├── survey_data_cleaning.py
│   └── survey_data_analysis.py
├── README.md
└── requirements.txt
```

## Tools Used
- Python (Pandas, OpenPyXL)
- Excel (for reviewing outputs)

## How to Run
1. Clone this repo
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the cleaning script:
   ```
   python scripts/survey_data_cleaning.py
   ```
4. Run the reporting script:
   ```
   python scripts/survey_data_analysis.py
   ```

## Skills Demonstrated
- Data quality assurance
- Survey data wrangling
- Summary statistics reporting
- Python automation for Excel outputs
