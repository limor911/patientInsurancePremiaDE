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
