import pandas as pd

csv_file_path = "C:/DE_Course/mid_project/patientInsurancePremiaDE/insurance_dataset.csv"

df = pd.read_csv(csv_file_path)

# List of column names
column_names = ["gender", "smoker", "medical_history", "coverage_level"]

# Initialize an empty dictionary to store column values
column_values_dict = {}

# Iterate through each column name
for col_name in column_names:
    # Extract values for the current column, convert them to a set to remove duplicates, then convert back to a list
    column_values = list(set(df[col_name]))
    
    # Store the column name as key and the unique values list as value in the dictionary
    column_values_dict[col_name] = column_values

txt_for_user = "Hi user" + '\n' + "please provide your detailes such as 'age',\
'gender', 'smoker', 'height_in_cm', 'weight_in_kg', 'medical_history' and the coverage level that you want"

txt_for_user_possible_values = "\n" + "That the possible values you can fill for each variable :"

text_guide_for_user = "\n" + "You can fill details for each of your family member, assign each one as 'pat_d_' plus digit." + "\n"\
"Member number one will assign to 'pat_d_1', member number two will assign to 'pat_d_2' ect" + "\n"\

text_example_for_user = "\n" + "Exmaple for only one member with the details :" + "\n"\
"age is 45, gender female, not smoke, height 168, weight 65, medical history Diabetes, coverage level is premium --->" + "\n"\
"pat_d_1 = Patient_details(45, 'female', 'no', 168, 65, 'Diabetes', 'Premium')" + "\n"\

print(txt_for_user)

print(txt_for_user_possible_values)

# Display the dictionary
print(column_values_dict)

print(text_example_for_user)


#Create a class for patient details
class Patient_details:
    def __init__(self, age: int, gender: str, smoker: str, height_in_cm: int, weight_in_kg: int, medical_history: str, coverage_level: str):
        # Age constraint
        if not 18 <= age <= 65:
            raise ValueError("Age must be between 18 and 65")
        
        # Gender constraint
        gender = gender.lower()  # Convert to lowercase for consistency
        if gender not in ['male', 'female']:
            raise ValueError("Gender must be 'Male' or 'Female'")

        smoker = smoker.lower()
        if smoker not in ['yes', 'no']:
            raise ValueError("Smoker must be 'yes' or 'no'")
        
        # Bmi constraint
        bmi = weight_in_kg/(height_in_cm/100)**2
        if not 18 <= bmi <= 50:
            raise ValueError(f"Your calculated Bmi is {bmi}" + '\n' + "Bmi calculated by height and weight, must be between 18 and 50")
       
       # medical_history constraint
        medical_history = medical_history.lower()
        if medical_history not in ["high blood pressure", "diabetes", "heart disease", ""]:
            raise ValueError("medical history must be one of 'High blood pressure', 'Diabetes', 'Heart disease' or empty")

       # coverage_level constraint
        coverage_level = coverage_level.lower()
        if coverage_level not in ['basic', 'standard', 'premium']:
            raise ValueError("coverage level must be one of 'Basic', 'Standard', 'Premium'")
        
        self.age = age
        self.gender = gender
        self.smoker = smoker
        self.height_in_cm = height_in_cm
        self.weight_in_kg = weight_in_kg
        self.bmi = weight_in_kg/(height_in_cm/100)**2
        self.medical_history = medical_history
        self.coverage_level = coverage_level

p = Patient_details(18, 'Male', 'yes', 1174, 65, '', 'basic')

print(p)