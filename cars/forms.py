from django import forms
from cars.models import Car
    
class NewCarModelForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        
    def clean_value(self): 
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Minimum car value is R$ 20000.')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Minimum car factory year is 1975')
        return factory_year