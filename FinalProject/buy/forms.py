from django import forms

from .models import Computer, Desktop, Laptop, Customer

class DesktopForm(forms.ModelForm):
    class Meta:
        model = Desktop
        fields = ("manufacturer", "operating_system", "ram", "storage_hdd", "storage_ssd", "has_monitor")

class LaptopForm(forms.ModelForm):
    class Meta:
        model = Laptop
        fields = ("manufacturer", "operating_system", "ram", "storage_hdd", "storage_ssd", "battery_life")

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("first_name", "last_name", "address", "email", "phone_number", "card_number")
