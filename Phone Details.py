import phonenumbers
from phonenumbers import timezone,geocoder,carrier
phone=input("Enter your phone numer with +__: ")
number=phonenumbers.parse(phone)
time=timezone.time_zones_for_number(number)
car=carrier.name_for_number(number,"en")
geo=geocoder.description_for_number(number,"en")
print(time)
print(geo)
print(car)