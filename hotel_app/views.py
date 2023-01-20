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
    Room_Occupancy_Details,
    Booking_status,
    Hall_Type,
    Mode_of_Payment,
    Payment_Type,
    Property_Details,
    Payment_Status
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
    Booking_Details_View_Serializer2,
    Property_Details_View_Serializer

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





class Room_Occupancy_View(APIView):
    def get(self,request,*args,**kwargs):
        if request.method == 'GET':
            datas = Room_Booking_Details.objects.all()
            data = [{
                "booking_id": i.booking_id,
                "no_of_rooms": i.no_of_rooms,
                "from_date": i.from_date,
                "to_date": i.to_date,
                "room_type": i.room_type.room_type,
                "username": i.user.username
            } for i in datas]
        return Response(data )


class Property_Details_View(APIView):
    serializer_class = Property_Details_View_Serializer

    def post(self, request, *args, **kwargs):
        try:
            details = Property_Details(
                property_id=request.data['property_id'],
                name=request.data['name'],
                address=request.data['address'],
            )
            details.save()
            serializer = Property_Details_View_Serializer(details)
            result = "Data updated successfully"
        except:
            serializer = Property_Details_View_Serializer()
            result = "An error occurred"
        return Response({'response': result, 'data': serializer.data})


class Booking_Person_Details_View(APIView):
    serializer_class = Booking_Person_Details_Serializer

    def post(self, request, *args, **kwargs):
        try:
            temp_user = request.data.get('user'),
            user = User.objects.get(id=temp_user[0])
            details = Booking_Person_Details(
                user=user,
                name=request.data["name"],
                mobile_no=request.data["mobile_no"],
                adhaar_no=request.data["adhaar_no"],
                email=request.data["email"]
            )
            details.save()
            serializer = Booking_Person_Details_Serializer(details)
            result = "Data updated successfully"
        except:
            serializer = Booking_Person_Details_Serializer()
            result = "An error occurred"
        return Response({'response': result, 'data': serializer.data})


class Room_Booking_Details_View(APIView):
    serializer_class = Room_Booking_Details_Serializer

    def get(self, request, *args, **kwargs):
        r_type = Room_Type.objects.all()
        data = [{
            "room_type": i.room_type
        } for i in r_type]
        return Response(data)

    def post(self, request, *args, **kwargs):
        try:
            temp_user = request.data.get('user'),
            user = User.objects.get(id=temp_user[0])
            temp_room_type = request.data.get('room_type'),
            room_type = Room_Type.objects.get(room_type=temp_room_type[0])
            details = Room_Booking_Details(
                user=user,
                booking_id=request.data["booking_id"],
                room_type=room_type,
                no_of_rooms=request.data["no_of_rooms"],
                from_date=request.data["from_date"],
                to_date=request.data["to_date"]
            )
            details.save()
            serializer = Room_Booking_Details_Serializer(details)
            result = "Data updated successfully"
        except:
            serializer = Room_Booking_Details_Serializer()
            result = "An error occurred"
        return Response({'response': result, 'data': serializer.data})


class Room_Details_View(APIView):
    serializer_class = Room_Details_Serializer

    def get(self, request, *args, **kwargs):
        r_type = Room_Type.objects.all()
        data = [{
            "room_type": i.room_type
        } for i in r_type]
        return Response(data)

    def post(self, request, *args, **kwargs):
        try:
            temp_room_prop = request.data['room_property_id']
            room_property_id = Property_Details.objects.get(property_id=temp_room_prop[0])
            temp_room_type = request.data['room_type'],
            print(temp_room_type)
            room_type = Room_Type.objects.get(room_type=temp_room_type[0])
            details = Room_Details(
                room_property_id=room_property_id,
                room_no=request.data["room_no"],
                room_type=room_type
            )
            details.save()
            serializer = Room_Details_Serializer(details)
            result = "Data updated successfully"
        except:
            serializer = Room_Details_Serializer()
            result = "An error occurred"
        return Response({'response': result, 'data': serializer.data})


class Booking_Details_View(APIView):
    serializer_class = Booking_Details_Serializer

    def get(self, request, *args, **kwargs):
        booking_id = Room_Booking_Details.objects.all()
        print(booking_id)
        data = [{
            "booking_id": i.booking_id
        } for i in booking_id]
        return Response(data)

    def post(self, request, *args, **kwargs):
        try:
            temp_user = request.data["user"],
            user = User.objects.get(id=temp_user[0])
            b_status = request.data["booking_status"]
            print(b_status)
            status = Booking_status.objects.get(booking_status=b_status)
            print(status)
            temp_bookingId = request.data['booking_id'],
            bookinID = Room_Booking_Details.objects.get(booking_id=temp_bookingId[0])
            details = Booking_Details(
                user=user,
                booking_id=bookinID,
                booking_amount=request.data["booking_amount"],
                booking_advance_amount=request.data["booking_advance_amount"],
                booking_status=status,
            )
            details.save()
            serializer = Booking_Details_Serializer(details)
            result = "Data updated successfully"
        except:
            serializer = Booking_Details_Serializer()
            result = "An error occurred"
        return Response({'response': result, 'data': serializer.data})


class Party_hall_Booking_View(APIView):
    serializer_class = Party_hall_Booking_Serializer

    def post(self, request, *args, **kwargs):
        try:
            temp_user = request.data.get('user'),
            user = User.objects.get(id=temp_user[0])
            temp_hall_type = request.data['hall_type'],
            hall_type = Hall_Type.objects.get(hall_type=temp_hall_type[0])
            details = Party_Hall_Booking_Details(
                user=user,
                booking_id=request.data["booking_id"],
                advance_amount=request.data["advance_amount"],
                hall_type=hall_type,
                rent_amount=request.data["rent_amount"],
                function_date=request.data["function_date"],
                function_time=request.data["function_time"],
                refered_by=request.data["refered_by"],
            )
            details.save()
            serializer = Party_hall_Booking_Serializer(details)
            result = "Data updated successfully"
        except:
            serializer = Party_hall_Booking_Serializer()
            result = "An error occurred"
        return Response({'response': result, 'data': serializer.data})


class Party_Hall_Payment_details_View(APIView):
    serializer_class = Party_Hall_Payment_details_Serializer

    def get(self, request, *args, **kwargs):
        booking_id = Party_Hall_Booking_Details.objects.all()
        data = [{
            "booking_id": i.booking_id
        } for i in booking_id]
        return Response(data)

    def post(self, request, *args, **kwargs):
        try:
            temp_user = request.data['user'],
            user = User.objects.get(id=temp_user[0])
            temp_MOP = request.data['mode_of_payment'],
            MOP = Mode_of_Payment.objects.get(mode_of_payment=temp_MOP[0])
            # temp_PT = request.data['payment_type'],
            # PT = Payment_Type.objects.get(payment_type=temp_PT[0])
            temp_bookingId = request.data['booking_id'],
            bookinID = Party_Hall_Booking_Details.objects.get(booking_id=temp_bookingId[0])
            temp_p_status = request.data['payment_status']
            p_status = Payment_Status.objects.get(payment_status=temp_p_status)
            details = Party_Hall_Payment_details(
                user=user,
                payment_id=request.data["payment_id"],
                amount=request.data["amount"],
                mode_of_payment=MOP,
                # payment_type=PT,
                date_time=request.data["date_time"],
                booking_id=bookinID,
                payment_status=p_status
            )
            details.save()
            serializer = Party_Hall_Payment_details_Serializer(details)
            result = "Data updated successfully"
        except:
            serializer = Party_Hall_Payment_details_Serializer()
            result = "An error occurred"
        return Response({'response': result, 'data': serializer.data})


class Room_Payment_details_View(APIView):
    serializer_class = Room_Payment_details_Serializer

    def get(self, request, *args, **kwargs):
        booking_id = Room_Booking_Details.objects.all()
        data = [{
            "booking_id": i.booking_id
        } for i in booking_id]
        return Response(data)

    def post(self, request, *args, **kwargs):
        try:
            temp_user = request.data.get('user'),
            user = User.objects.get(id=temp_user[0])
            temp_MOP = request.data.get('mode_of_payment'),
            MOP = Mode_of_Payment.objects.get(mode_of_payment=temp_MOP[0])
            # temp_PT = request.data.get('payment_type'),
            # PT = Payment_Type.objects.get(payment_type=temp_PT[0])
            temp_bookingId = request.data.get('booking_id'),
            bookinID = Room_Booking_Details.objects.get(booking_id=temp_bookingId[0])
            print(request.data)
            temp_p_status = request.data['payment_status']
            p_status = Payment_Status.objects.get(payment_status=temp_p_status)
            details = Room_Payment_details(
                user=user,
                payment_id=request.data["payment_id"],
                amount=request.data["amount"],
                mode_of_payment=MOP,
                # payment_type=PT,
                date_time=request.data["date_time"],
                booking_id=bookinID,
                payment_status=p_status
            )
            details.save()
            serializer = Room_Payment_details_Serializer(details)
            result = "Data updated successfully"
        except:
            serializer = Room_Payment_details_Serializer()
            result = "An error occurred"
        return Response({'response': result, 'data': serializer.data})
