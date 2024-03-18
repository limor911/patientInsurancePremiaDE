import pandas as pd

csv_file_path = "C:/DE_Course/mid_project/patientInsurancePremiaDE/insurance_dataset.csv"

print(csv_file_path)

df = pd.read_csv(csv_file_path)

print(df.head())