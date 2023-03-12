from django.shortcuts import render
from .forms import DesktopForm, LaptopForm, CustomerForm
import csv

# Create your views here.

def buy(request):
    return render(request, "buy/buy.html")

def desktop(request):
    if request.POST:
        form_desktop = DesktopForm(request.POST)
        form_customer = CustomerForm(request.POST)
        if form_desktop.is_valid() and form_customer.is_valid():
            manufacturer = form_desktop.cleaned_data["manufacturer"]
            operating_system = form_desktop.cleaned_data["operating_system"]
            ram = form_desktop.cleaned_data["ram"]
            storage_hdd = form_desktop.cleaned_data["storage_hdd"]
            storage_ssd = form_desktop.cleaned_data["storage_ssd"]
            has_monitor = form_desktop.cleaned_data["has_monitor"]
            first_name = form_customer.cleaned_data["first_name"]
            last_name = form_customer.cleaned_data["last_name"]
            address = form_customer.cleaned_data["address"]
            email = form_customer.cleaned_data["email"]
            phone_number = form_customer.cleaned_data["phone_number"]
            card_number = form_customer.cleaned_data["card_number"]
            with open("purchases.csv", "a") as toFile:
                writer = csv.writer(toFile)
                writer.writerow([manufacturer, operating_system, ram, storage_hdd, storage_ssd, has_monitor, first_name, last_name, address, email, phone_number, card_number])
                toFile.close()
            with open("purchases.csv", "r") as fromFile:
                reader = csv.reader(fromFile)
                all_rows = [r for r in reader]
                row = all_rows[-1]
                price = 300
                price += int(row[2]) * 5 #ram
                price += int(row[3]) / 5 #storage_hdd
                price += int(row[4]) / 5 #storage_ssd
                if row[5] == "True":
                    price += 100 #has_monitor
                fromFile.close()
            return render(request, "buy/confirm.html", {"price": format(price, ".2f")})
        else:
            error = "Sorry, there was an error processing your form"
            form_desktop = DesktopForm()
            form_customer = CustomerForm
            return render(request, "buy/desktop.html", {"error": error})
    return render(request, "buy/desktop.html")

def laptop(request):
    if request.POST:
        form_laptop = LaptopForm(request.POST)
        form_customer = CustomerForm(request.POST)
        print(form_laptop.is_valid())
        if form_laptop.is_valid() and form_customer.is_valid():
            manufacturer = form_laptop.cleaned_data["manufacturer"]
            operating_system = form_laptop.cleaned_data["operating_system"]
            ram = form_laptop.cleaned_data["ram"]
            storage_hdd = form_laptop.cleaned_data["storage_hdd"]
            storage_ssd = form_laptop.cleaned_data["storage_ssd"]
            battery_life = form_laptop.cleaned_data["battery_life"]
            first_name = form_customer.cleaned_data["first_name"]
            last_name = form_customer.cleaned_data["last_name"]
            address = form_customer.cleaned_data["address"]
            email = form_customer.cleaned_data["email"]
            phone_number = form_customer.cleaned_data["phone_number"]
            card_number = form_customer.cleaned_data["card_number"]
            with open("purchases.csv", "a") as toFile:
                writer = csv.writer(toFile)
                writer.writerow([manufacturer, operating_system, ram, storage_hdd, storage_ssd, battery_life, first_name, last_name, address, email, phone_number, card_number])
                toFile.close()
            with open("purchases.csv", "r") as fromFile:
                reader = csv.reader(fromFile)
                all_rows = [r for r in reader]
                row = all_rows[-1]
                price = 200
                price += int(row[2]) * 5 #ram
                price += int(row[3]) / 5 #storage_hdd
                price += int(row[4]) / 5 #storage_ssd
                price += int(row[5]) * 3 #battery_life
                fromFile.close()
            return render(request, "buy/confirm.html", {"price": format(price, ".2f")})
        else:
            error = "Sorry, there was an error processing your form"
            form_laptop = LaptopForm()
            form_customer = CustomerForm()
            return render(request, "buy/laptop.html", {"error": error})
    return render(request, "buy/laptop.html")

def thanks(request):
    return render(request, "buy/thanks.html")
