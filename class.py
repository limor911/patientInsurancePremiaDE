import pandas as pd

# Create a class for patient details
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
            self.gender = input("Enter gender (M/F): ").lower()
            if self.gender in ['m', 'f']:
                break
            else:
                print("Gender must be 'M' or 'F'")

    def enter_smoker(self):
        while True:
            self.smoker = input("Are you a smoker? (Y/N): ").lower()
            if self.smoker in ['y', 'n']:
                break
            else:
                print("Smoker must be 'Y' or 'N'")

    def enter_height_and_weight(self):
        while True:
            try:
                self.height_in_cm = int(input("Enter height in cm: "))
                self.weight_in_kg = int(input("Enter weight in kg: "))

                # Bmi constraint
                self.bmi =  int(self.weight_in_kg / (self.height_in_cm / 100) ** 2)
                if not 18 <= self.bmi <= 50:
                    raise ValueError(f"Your calculated BMI is {self.bmi}\nBMI calculated by height and weight, must be between 18 and 50")
                break
            except ValueError as e:
                print(e)

    def enter_medical_history(self):
        while True:
            self.medical_history = input("Enter medical history (High blood pressure / Diabetes / Heart disease or leave blank if none): ").lower()
            if self.medical_history in ["high blood pressure", "diabetes", "heart disease", ""]:
                break
            else:
                print("Medical history must be one of 'High blood pressure', 'Diabetes', 'Heart disease' or empty")

    def enter_coverage_level(self):
        while True:
            self.coverage_level = input("Enter coverage level (Basic / Standard / Premium): ").lower()
            if self.coverage_level in ['basic', 'standard', 'premium']:
                break
            else:
                print("Coverage level must be one of 'Basic', 'Standard', 'Premium'")
                
    def calculate_charges(self):
        # Charges calculation based on different factors
        base_charge = 100  # Base charge
        age_charge = 0
        if self.age < 25:
            age_charge = 20
        elif self.age >= 45:
            age_charge = 50
        
        smoker_charge = 0
        if self.smoker == 'yes':
            smoker_charge = 100
        
        bmi_charge = 0
        if self.bmi > 30:
            bmi_charge = 30
        
        medical_history_charge = 0
        if self.medical_history:
            medical_history_charge = 50
        
        coverage_level_charge = 0
        if self.coverage_level == 'standard':
            coverage_level_charge = 30
        elif self.coverage_level == 'premium':
            coverage_level_charge = 50
        
        self.charges = base_charge + age_charge + smoker_charge + bmi_charge + medical_history_charge + coverage_level_charge

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
    patient.calculate_charges()

    patient_data.append(patient)

    another_entry = input("Do you want to enter details for another patient? (yes/no): ").lower()
    if another_entry != 'yes':
        break

# Create DataFrame from the list of patient details with selected columns
column_names = ["age","gender", "smoker", "bmi","medical_history", "coverage_level", "charges"]
df_pat = pd.DataFrame([{col: getattr(p, col) for col in column_names} for p in patient_data])

# Save DataFrame to a CSV file
df_pat.to_csv("patient_details.csv", index=False)



# Check if there is only one record in the DataFrame
# Check if there is only one record in the DataFrame
if len(df_pat) == 1:
    print(f"According to our calculation, your charges are: {df_pat['charges'].iloc[0]}")
else:
    print("According to our calculation, these are your family charges:")
    for index, row in df_pat.iterrows():
        print(f"Patient {index + 1}: Gender: {row['gender']}, Smoker: {row['smoker']}, BMI: {row['bmi']}, Medical History: {row['medical_history']}, Coverage Level: {row['coverage_level']}  ")
        print(f"Charges: {row['charges']}")
        print()  # Add a blank line between each patient's details

