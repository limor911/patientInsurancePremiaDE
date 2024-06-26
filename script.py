import pandas as pd
import os
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

###### part 1#### creating reports for dataset 
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

# If this file is run directly
if __name__ == "__main__":
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

# If this file is run directly
#if __name__ == "__main__":
    df.head()

# Define a function to format y-axis labels with separated thousands
def format_thousands(x, pos):
    return '{:,.0f}'.format(x)

# If this file is run directly
#if __name__ == "__main__":
# Loop through each column in the DataFrame

for column in df.columns:
    if column != 'charges':  # Exclude column 'charges'
    # Count the frequency of each unique value in the column
        value_counts = df[column].value_counts()

    # Sort the values by index (the unique values in the column)
    alue_counts_sorted = value_counts.sort_index()
        
    # Plot the bar graph
    plt.figure(figsize=(10, 6))  # Adjust the figure size if needed
    ax = alue_counts_sorted.plot(kind='bar')
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
    corr_coef = df['charges'].corr(df[column])
    corr_coef = corr_coef.round(3)*100

    print(f'Correlation coefficient between charges and {column}: {corr_coef}%')
#part 2#### Create a class for patient details 

class Patient_details:
    def __init__(self):
        self.age = None
        self.gender = None
        self.smoker = None
        self.height_in_cm = None
        self.weight_in_kg = None
        self.bmi = None
        self.medical_history = None
        self.coverage_level = None
        self.charges = None

    def enter_age(self):
        while True:
            try:
                self.age = int(input("Enter age: "))
                if not 18 <= self.age <= 65:
                    raise ValueError("Age must be between 18 and 65")
                break
            except ValueError as e:
                print(e)

    def enter_gender(self):
        while True:
            try:
                print("\nGender options:")
                print("0: Male")
                print("1: Female")
                gender_input = int(input("Enter gender: "))
                if gender_input in [0, 1]:
                    self.gender = 'male' if gender_input == 0 else 'female'
                    break
                else:
                    print("Invalid input. Please enter 0 for Male or 1 for Female.")
            except ValueError:
                print("Invalid input. Please enter 0 for Male or 1 for Female.")

    def enter_smoker(self):
        while True:
            try:
                print("\nSmoker options:")
                print("0: No")
                print("1: Yes")
                smoker_input = int(input("Are you a smoker?: "))
                if smoker_input in [0, 1]:
                    self.smoker = 'yes' if smoker_input == 1 else 'no'
                    break
                else:
                    print("Invalid input. Please enter 0 for 'no' or 1 for 'yes'.")
            except ValueError:
                print("Invalid input. Please enter 0 for 'no' or 1 for 'yes'.")

    def enter_height_and_weight(self):
        while True:
            try:
                self.height_in_cm = int(input("\nEnter height in cm: "))
                self.weight_in_kg = int(input("\nEnter weight in kg: "))

                # Bmi constraint
                self.bmi = int(self.weight_in_kg / (self.height_in_cm / 100) ** 2)
                if not 18 <= self.bmi <= 50:
                    raise ValueError(f"Your calculated BMI is {self.bmi}\nBMI calculated by height and weight, must be between 18 and 50")
                break
            except ValueError as e:
                print(e)

    def enter_medical_history(self):
        while True:
            try:
                print("\nMedical history options:")
                print("0: None")
                print("1: High blood pressure")
                print("2: Diabetes")
                print("3: Heart disease")

                medical_history_input = int(input("Enter corresponding number for medical history: "))
                if medical_history_input in [0, 1, 2, 3]:
                    if medical_history_input == 0:
                        self.medical_history = "none"
                    elif medical_history_input == 1:
                        self.medical_history = "high_blood_pressure"
                    elif medical_history_input == 2:
                        self.medical_history = "diabetes"
                    elif medical_history_input == 3:
                        self.medical_history = "heart_disease"
                    break
                else:
                    print("Invalid input. Please enter a number between 0 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number between 0 and 3.")

    def enter_coverage_level(self):
        while True:
            try:
                print("\nCoverage level options:")
                print("1: Basic")
                print("2: Standard")
                print("3: Premium")
                coverage_input = int(input("Enter corresponding number for coverage level: "))
                if coverage_input in [1, 2, 3]:
                    if coverage_input == 1:
                        self.coverage_level = 'basic'
                    elif coverage_input == 2:
                        self.coverage_level = 'standard'
                    elif coverage_input == 3:
                        self.coverage_level = 'premium'
                    break
                else:
                    print("Invalid input. Please enter a number between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 3.")


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

    patient_data.append(patient)


    print("\nDo you want to enter details for another patient?")
    print("0: No")
    print("1: Yes")
    another_entry = int(input("Enter your choice: "))
    if another_entry != 1:
        break

#part 3##### Create simulator for answer 
# Create DataFrame from the list of patient details with selected columns
column_names = ["age", "bmi", "gender", "smoker", "medical_history", "coverage_level"]
df_pat = pd.DataFrame([{col: getattr(p, col) for col in column_names} for p in patient_data])

# Save DataFrame to a CSV file
df_pat.to_csv("patient_details.csv", index=False)


# Calculate charges for df_pat based on mean charges of df
# The calculation based on patient data like age, gender, ect.
charges_list = []
for index, row in df_pat.iterrows():
    # Define the range for age and bmi
    age_range = range(row['age'] - 2, row['age'] + 3)
    bmi_range = range(row['bmi'] - 2, row['bmi'] + 3)

    # Filter df based on the defined ranges and other conditions
    filtered_df = df[
        (df['age'].isin(age_range)) &
        (df['bmi'].isin(bmi_range)) &
        (df['gender'] == row['gender']) &
        (df['smoker'] == row['smoker']) &
        (df['medical_history'] == row['medical_history']) &
        (df['coverage_level'] == row['coverage_level'])
    ]

    if not filtered_df.empty:
        mean_charge = int(filtered_df['charges'].mean())
        charges_list.append(mean_charge)
    else:
        charges_list.append(None)

df_pat['calculated_charges_int'] = charges_list

# Add thousand separators to the 'numbers' column and concatenate '$' sign
df_pat['calculated_charges'] = '$' + df_pat['calculated_charges_int'].map('{:,.0f}'.format)

#List all relevant columns to patient
relvant_columns = ['age', 'bmi', 'gender', 'smoker', 'medical_history', 'coverage_level', 'calculated_charges']

print("\nAccording to our SIMULATOR, That the details of all users and thier calculate charges:")
#df_pat[relvant_columns].head(50)
print(df_pat[relvant_columns].head(50))