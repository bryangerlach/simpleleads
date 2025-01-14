from django import forms

class LeadForm(forms.Form):
    company = forms.CharField(label="Company", required=False)
    contact = forms.CharField(label="Contact", required=False)
    date = forms.DateField(label="Date", required=False)
    installed = forms.BooleanField(required=False)
    verbal = forms.BooleanField(required=False)
    invoice = forms.BooleanField(required=False)
    paid = forms.BooleanField(required=False)
    phone = forms.CharField(label="Phone", required=False)
    address = forms.CharField(label="Address", required=False)
    notes = forms.CharField(label="Notes", required=False)
    stale = forms.BooleanField(required=False)
    probable = forms.BooleanField(required=False)
    trial = forms.BooleanField(required=False)
    trial_expiration = forms.DateField(required=False)