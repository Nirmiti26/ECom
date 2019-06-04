from django import forms


class PVForm(forms.Form):
    pincode = forms.IntegerField()
    system_load = forms.IntegerField()
    monthly_bill = forms.IntegerField()
    roof_area = forms.IntegerField()

