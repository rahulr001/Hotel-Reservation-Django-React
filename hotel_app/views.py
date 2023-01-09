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
    Room_Type,
    Room_Occupancy_Details
)
from django.contrib.auth.models import User
from rest_framework.response import Response
from .serializer import (
    Room_Details_Serializer,
    Room_Occupancy_Serializer,
    Room_Booking_Details_Serializer,
    Room_Payment_details_Serializer,
    Party_hall_Booking_Serializer,
    Party_Hall_Payment_details_Serializer,
    Booking_Details_Serializer,
    Booking_Person_Details_Serializer,
    Booking_Details_View_Serializer,
    Booking_Details_View_Serializer2
)
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated

api_view(['GET'])


def Booking_Details_ViewList(request):
    if request.method == "GET":
        datas = Booking_Details.objects.all()
        datas2 = Room_Booking_Details.objects.all()
        serializer = Booking_Details_View_Serializer(datas, many=True).data
        serializer2 = Booking_Details_View_Serializer2(datas2, many=True).data
        serializer.append(serializer2)
    return JsonResponse(serializer, safe=False)


api_view(['GET'])


def Room_Occupancy_View(request):
    if request.method == 'GET':
        datas = Room_Booking_Details.objects.all()
        serializer = Room_Occupancy_Serializer(datas, many=True)
    return JsonResponse(serializer.data, safe=False)


class Booking_Person_Details_View(CreateAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class=Booking_Person_Details_Serializer
    # def create(self,request,*args,**kwargs):
    #     serializer=self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     res = "Data updated successfully"
    #     return Response({'response': res })
    def post(self, request):
        # serializer=Booking_Person_Details_Serializer(request.data)
        # data = request.data
        # print(data)
        # print(request.user)
        # print(serializer)
        # print(serializer.data)
        # details = Booking_Person_Details(
        #     serializer.data
        # )
        details = Booking_Person_Details (
            user=request.user,
            name=request.data["name"],
            mobile_no=request.data["mobile_no"],
            adhaar_no=request.data["adhaar_no"],
            email=request.data["email"]
        )
        details.save()
        serializer=Booking_Person_Details_Serializer(details)
        print(details)
        res = "Data updated successfully"
        # except:
        #     res = "oops error"
        #     details = 'oops'
        return Response({'response': res, 'data': serializer.data})
#
# class Booking_Person_Details_View(CreateAPIView):
#     serializer_class = Booking_Person_Details_Serializer
#
#     def post(self, request, *args, **kwargs):
#         serializer = Booking_Person_Details_Serializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#         return JsonResponse(serializer.data)


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
    serializer_class = Room_Payment_details_Serializer

    def post(self, request, *args, **kwargs):
        serializer = Room_Payment_details_Serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return JsonResponse(serializer.data)




















