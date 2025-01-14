from django.db import models
from django.contrib.auth.models import User

class Lead(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    company = models.CharField(max_length=100)
    contact = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)
    installed = models.BooleanField(default = False)
    verbal = models.BooleanField(default = False)
    invoice = models.BooleanField(default = False)
    paid = models.BooleanField(default = False)
    phone = models.CharField(max_length=10, null=True)
    address = models.CharField(max_length=150, null=True)
    notes = models.CharField(max_length=1000, null=True)
    stale = models.BooleanField(default = False)
    probable = models.BooleanField(default = False)
    trial = models.BooleanField(default = False)
    trial_expiration = models.DateField(null=True, blank=True)

    def add_lead(self, data, user):
        self.user = user
        self.company = data['company']
        self.contact = data['contact']
        self.date = data['date']
        self.installed = data['installed']
        self.verbal = data['verbal']
        self.invoice = data['invoice']
        self.paid = data['paid']
        self.phone = data['phone']
        self.address = data['address']
        self.notes = data['notes']
        self.stale = data['stale']
        self.probable = data['probable']
        self.trial = data['trial']
        self.trial_expiration = data['trial_expiration']

        self.save()