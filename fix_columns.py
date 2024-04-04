import pandas as pd
import matplotlib.pyplot as plt

csv_file_path = "C:/DE_Course/mid_project/patientInsurancePremiaDE/insurance_dataset.csv"

df = pd.read_csv(csv_file_path)

"""
שינוי עמודות ערכי עמודות שיש בהן טקסט עם רווחים ל-'_'
הצגת גרפים על התפלגויות המבוטחים
עיגול לטובה של עמודת BMI
אופציה - לולאה של גרפים עם התפלגות כמויות
עיגול לטובה של עמודה charges
"""

print(df.head())

# Replace spaces with underscores in all columns of the DataFrame
df.replace(' ', '_', regex=True, inplace=True)

print(df.head())


# Loop through each column in the DataFrame
for column in df.columns:
    if column != 'charges':  # Exclude col_b
        # Count the frequency of each unique value in the column
        value_counts = df[column].value_counts()
        
        # Sort the values by index (the unique values in the column)
        value_counts_sorted = value_counts.sort_index()
        
        # Plot the bar graph
        plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
        value_counts_sorted.plot(kind='bar')
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
        plt.show()