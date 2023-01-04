from .models import (
    Booking_Person_Details,
    Property_Details,
    Booking_Details,
    Room_Details,
    Room_Booking_Details,
    Party_hall_Booking_Details,
    Room_Payment_details,
    Party_Hall_Payment_details,
    Room_Occupancy_Details
)
from rest_framework import serializers


class Booking_Person_Details_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Booking_Person_Details
        fields = ['name', 'mobile_no', 'adhaar_no', 'email']


class Room_Booking_Details_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Room_Booking_Details
        fields = ['oyo_booking_id', 'room_type', 'no_of_rooms', 'from_date', 'to_date']


class Room_Details_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Room_Details
        fields = ['room_property_id', 'room_no', 'room_type']


class Booking_Details_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Booking_Details
        fields = ['booking_id ', 'booking_date_time ', 'booking_amount', 'booking_advance_amount', 'booking_status']


class Room_Payment_details_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Room_Payment_details
        fields = ['payment_id', 'amount', 'mode_of_payment', 'payment_type', 'date_time', 'booking_id']


class Room_Occupancy_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Room_Occupancy_Details
        fields = ['booking_id ', 'room_id ']


class Party_hall_Booking_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Party_hall_Booking_Details
        fields = ['booking_id ', 'date_and_time', 'advance_amount', 'hall_type', 'rent_amount', 'function_date ',
                  'function_time ', 'refered_by']


class Party_Hall_Payment_details_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Party_Hall_Payment_details
        fields = ['payment_id', 'amount', 'mode_of_payment', 'payment_type', 'date_time', 'booking_id']

