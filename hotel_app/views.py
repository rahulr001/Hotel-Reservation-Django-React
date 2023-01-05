from rest_framework.decorators import api_view
from .models import (
    Booking_Person_Details,
    Property_Details,
    Booking_Details,
    Room_Details,
    Room_Booking_Details,
    Party_Hall_Booking_Details,
    Room_Payment_details,
    Party_Hall_Payment_details,
    Room_Occupancy_Details
)
from .serializer import (
    Room_Details_Serializer,
    Room_Occupancy_Serializer,
    Room_Booking_Details_Serializer,
    Room_Payment_details_Serializer,
    Party_hall_Booking_Serializer,
    Party_Hall_Payment_details_Serializer,
    Booking_Details_Serializer,
    Booking_Person_Details_Serializer,
    Booking_Details_View_Serializer
)
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from django.http import JsonResponse


class Booking_Details_ViewList(ListAPIView):
    serializer_class = Booking_Details_View_Serializer
    queryset = Booking_Details.objects.all()


class Booking_Person_Details_View(CreateAPIView):
    serializer_class = Booking_Person_Details_Serializer

    def post(self, request, *args, **kwargs):
        serializer = Booking_Person_Details_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data)


class Room_Booking_Details_View(CreateAPIView):
    serializer_class = Room_Booking_Details_Serializer

    def post(self, request, *args, **kwargs):
        serializer = Room_Booking_Details_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data)


class Room_Details_View(CreateAPIView):
    serializer_class = Room_Details_Serializer

    def post(self, request, *args, **kwargs):
        serializer = Room_Details_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data)


class Booking_Details_View(CreateAPIView):
    serializer_class = Booking_Details_Serializer

    def post(self, request, *args, **kwargs):
        serializer = Booking_Details_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data)


class Room_Occupancy_View(CreateAPIView):
    serializer_class = Room_Occupancy_Serializer

    def post(self, request, *args, **kwargs):
        serializer = Room_Occupancy_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data)


class Party_hall_Booking_View(CreateAPIView):
    serializer_class = Party_hall_Booking_Serializer

    def post(self, request, *args, **kwargs):
        serializer = Party_hall_Booking_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data)


class Party_Hall_Payment_details_View(CreateAPIView):
    serializer_class = Party_Hall_Payment_details_Serializer

    def post(self, request, *args, **kwargs):
        serializer = Party_Hall_Payment_details_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data)


class Room_Payment_details_View(CreateAPIView):
    serializer_class = Party_Hall_Payment_details_Serializer

    def post(self, request, *args, **kwargs):
        serializer = Room_Payment_details_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data)
