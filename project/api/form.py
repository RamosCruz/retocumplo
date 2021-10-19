from django import forms
import datetime

class HomeForm(forms.Form):
    fechaIni=forms.DateField(initial=datetime.date.today)
    fechaFin=forms.DateField(initial=datetime.date.today)