from django.contrib import admin
from .models import (
    Booking_Person_Details,
    Property_Details,
    Booking_Details,
    Room_Details,
    Room_Booking_Details,
    Party_Hall_Booking_Details,
    Room_Payment_details,
    Party_Hall_Payment_details,
    Booking_status,
    Payment_Status,
    Mode_of_Payment,
    Payment_Type,
    Room_Type,
    Hall_Type,
)

admin.site.register(Booking_Person_Details)
admin.site.register(Property_Details)
admin.site.register(Booking_Details)
admin.site.register(Room_Details)
admin.site.register(Room_Booking_Details)
admin.site.register(Party_Hall_Booking_Details)
admin.site.register(Room_Payment_details)
admin.site.register(Party_Hall_Payment_details)
admin.site.register(Booking_status)
admin.site.register(Payment_Status)
admin.site.register(Mode_of_Payment)
admin.site.register(Payment_Type)
admin.site.register(Room_Type)
admin.site.register(Hall_Type)