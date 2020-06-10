from django import forms
from car_app.models import Car


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = (
            'manufacturer',
            'car_model',
            'production_year',
            'transmission',
            'car_color'
        )