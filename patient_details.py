import pandas as pd

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

    def create_df_pat(self, patient_data):
        # Create DataFrame from the list of patient details with selected columns
        column_names = ["age", "gender", "smoker", "bmi", "medical_history", "coverage_level", "charges"]
        return pd.DataFrame([{col: getattr(p, col) for col in column_names} for p in patient_data])
