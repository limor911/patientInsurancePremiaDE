import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

def csv_drive_path_generatoer(url):
 '''
 Help in read csv file directly from google drive.
 Make sure the csv format is standard.
 url:str - path to csv file example:
   url = 'https://drive.google.com/file/d/126JPZ3lYwdLyJ2d_7jxM9jMtZaOlF-Ld/view?usp=sharing'
 return : str
 '''
 path = 'https://drive.google.com/uc?export=download&id='+url.split('/')[-2]
 return path

link = "https://drive.google.com/file/d/1fKeW4q_bPyMH7mbVTj0-1mqtsBtk5428/view?usp=drive_link"
path = csv_drive_path_generatoer(url = link)
df = pd.read_csv(path)
print(df.head())

# Randomly sample 300,000 rows from the DataFrame
df = df.sample(n=300000)

df.replace(' ', '_', regex=True, inplace=True)


# Round values to nearest
df['charges'] = df['charges'].round().astype(int)

df['bmi'] = df['bmi'].round().astype(int)

#List of string columns
list_of_string_columns = ['gender', 'smoker',	'region',	'medical_history',	'family_medical_history',	'exercise_frequency',	'occupation',	'coverage_level']

# Loop through each column
for column in list_of_string_columns:
    # Convert values to lowercase
    df[column] = df[column].apply(lambda x: x.lower() if isinstance(x, str) else x)

df.head()

'''Fix columns
Replace spaces with underscores
Round values for bmi
Round values for charges'''

# Replace spaces with underscores in all columns of the DataFrame
df.replace(' ', '_', regex=True, inplace=True)


# Round values to nearest
df['charges'] = df['charges'].round().astype(int)

df['bmi'] = df['bmi'].round().astype(int)

#List of string columns
list_of_string_columns = ['gender', 'smoker',	'region',	'medical_history',	'family_medical_history',	'exercise_frequency',	'occupation',	'coverage_level']

# Loop through each column
for column in list_of_string_columns:
    # Convert values to lowercase
    df[column] = df[column].apply(lambda x: x.lower() if isinstance(x, str) else x)

df.head()

# Define a function to format y-axis labels with separated thousands
def format_thousands(x, pos):
    return '{:,.0f}'.format(x)

# Loop through each column in the DataFrame
for column in df.columns:
    if column != 'charges':  # Exclude column 'charges'
        # Count the frequency of each unique value in the column
        value_counts = df[column].value_counts()

        # Sort the values by index (the unique values in the column)
        value_counts_sorted = value_counts.sort_index()

        # Plot the bar graph
        plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
        ax = value_counts_sorted.plot(kind='bar')
        plt.title(f'Distribution of {column}')
        plt.xlabel(column)
        plt.ylabel('Frequency')
        plt.xticks(rotation=60)  # Rotate x-axis labels for better readability

        # Format y-axis labels with separated thousands
        ax.yaxis.set_major_formatter(FuncFormatter(format_thousands))
        plt.show()

        # List of columns to analyze
columns_to_analyze = ['age', 'children', 'bmi']

# Loop through each column
for column in columns_to_analyze:
    # Correlation coefficient
    corr_coef = sub_df['charges'].corr(sub_df[column])
    corr_coef = corr_coef.round(3)*100

    print(f'Correlation coefficient between charges and {column}: {corr_coef}%')