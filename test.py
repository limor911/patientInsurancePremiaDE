import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
from patient_details import Patient_details, CalculateCharges
from reports import csv_drive_path_generatoer

# Function to generate CSV drive path
def generate_csv_drive_path(url):
    path = csv_drive_path_generatoer(url)
    return path

# Function to read CSV data
def read_csv_data(path):
    df = pd.read_csv(path)
    return df

# Function to preprocess DataFrame
def preprocess_dataframe(df):
    # Randomly sample 300,000 rows from the DataFrame
    df = df.sample(n=300000)

    # Replace spaces with underscores in all columns of the DataFrame
    df.replace(' ', '_', regex=True, inplace=True)

    # Round values to nearest
    df['charges'] = df['charges'].round().astype(int)
    df['bmi'] = df['bmi'].round().astype(int)

    # List of string columns
    list_of_string_columns = ['gender', 'smoker', 'region', 'medical_history', 'family_medical_history', 'exercise_frequency', 'occupation', 'coverage_level']

    # Convert string values to lowercase
    for column in list_of_string_columns:
        df[column] = df[column].apply(lambda x: x.lower() if isinstance(x, str) else x)

    return df

# Function to plot distribution of categorical columns
def plot_categorical_distribution(df):
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

# Function to analyze correlation
def analyze_correlation(df):
    # List of columns to analyze
    columns_to_analyze = ['age', 'children', 'bmi']

    # Loop through each column
    for column in columns_to_analyze:
        # Correlation coefficient
        corr_coef = df['charges'].corr(df[column])
        corr_coef = corr_coef.round(3) * 100

        print(f'Correlation coefficient between charges and {column}: {corr_coef}%')

def main():
    # Initialize an empty list to hold patient details
    patient_data = []

    # Ask user for patient details
    while True:
        patient = Patient_details()
        patient.enter_age()
        patient.enter_gender()
        patient.enter_smoker()
        patient.enter_height_and_weight()
        patient.enter_medical_history()
        patient.enter_coverage_level()
        CalculateCharges.calculate_charges(patient)  # Calculate charges

        patient_data.append(patient)

        another_entry = input("Do you want to enter details for another patient? (yes/no): ").lower()
        if another_entry != 'yes':
            break

    # Create DataFrame
    df_pat = Patient_details().create_df_pat(patient_data)

    # Save DataFrame to a CSV file
    df_pat.to_csv("patient_details.csv", index=False)

    # Check if there is only one record in the DataFrame
    if len(df_pat) == 1:
        print(f"According to our calculation, your charges are: {df_pat['charges'].iloc[0]}")
    else:
        print("According to our calculation, these are your family charges:")
        for index, row in df_pat.iterrows():
            print(f"Patient {index + 1}: Gender: {row['gender']}, Smoker: {row['smoker']}, BMI: {row['bmi']}, Medical History: {row['medical_history']}, Coverage Level: {row['coverage_level']}  ")
            print(f"Charges: {row['charges']}")
            print()  # Add a blank line between each patient's details

    # Generate CSV drive path
    link = "https://drive.google.com/file/d/1fKeW4q_bPyMH7mbVTj0-1mqtsBtk5428/view?usp=drive_link"
    path = generate_csv_drive_path(link)

    # Read CSV data
    df = read_csv_data(path)

    # Preprocess DataFrame
    df = preprocess_dataframe(df)

    # Plot distribution of categorical columns
    plot_categorical_distribution(df)

    # Analyze correlation
    analyze_correlation(df)

if __name__ == "__main__":
    main()
