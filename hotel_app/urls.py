from django.urls import path, include
from .views import (
    Booking_Person_Details_View,
    Room_Booking_Details_View,
    Booking_Details_ViewList,
    Room_Details_View,
    Booking_Details_View,
    Room_Occupancy_View,
    Party_hall_Booking_View,
    Party_Hall_Payment_details_View,
    Room_Payment_details_View,

)

urlpatterns = [
    path('bookingPerson/',Booking_Person_Details_View.as_view(), name="bookingPerson"),
    path('roomDetails/', Room_Details_View.as_view(), name="roomDetails"),
    path('roomBooking/', Room_Booking_Details_View.as_view(), name="roomBooking"),
    path('roomBookingDetails/', Booking_Details_ViewList.as_view(), name="roomBookingDetails"),
    path('bookingDetails/', Booking_Details_View.as_view(), name='bookingDetails'),
    path('roomOccupancy/', Room_Occupancy_View.as_view(), name="roomOccupancy"),
    path('partyHallBooking/', Party_hall_Booking_View.as_view(), name="partyHallBooking"),
    path('partyHallPayment/', Party_Hall_Payment_details_View.as_view(), name="partyHallPayment"),
    path('roomPayment/', Room_Payment_details_View.as_view(), name="roomPayment"),
]
