class CalculateCharges:
    @staticmethod
    def calculate_charges(patient):
        # Charges calculation based on different factors
        base_charge = 100  # Base charge
        age_charge = 0
        if patient.age < 25:
            age_charge = 20
        elif patient.age >= 45:
            age_charge = 50
        
        smoker_charge = 0
        if patient.smoker == 'yes':
            smoker_charge = 100
        
        bmi_charge = 0
        if patient.bmi > 30:
            bmi_charge = 30
        
        medical_history_charge = 0
        if patient.medical_history:
            medical_history_charge = 50
        
        coverage_level_charge = 0
        if patient.coverage_level == 'standard':
            coverage_level_charge = 30
        elif patient.coverage_level == 'premium':
            coverage_level_charge = 50
        
        patient.charges = base_charge + age_charge + smoker_charge + bmi_charge + medical_history_charge + coverage_level_charge
