from patient_details import Patient_details
from calculate_charges import CalculateCharges
from reports import csv_drive_path_generatoer





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
    print(f"\nAccording to our SIMULATOR, your charges are: {df_pat['charges'].iloc[0]}")
else:
    print("\nAccording to our SIMULATOR, these are your family charges:")
    for index, row in df_pat.iterrows():
        print(f"Patient {index + 1}: Gender: {row['gender']}, Smoker: {row['smoker']}, BMI: {row['bmi']}, Medical History: {row['medical_history']}, Coverage Level: {row['coverage_level']}  ")
        print(f"Charges: {row['charges']}")
        print()  # Add a blank line between each patient's details
