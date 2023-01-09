from django.db import models
from django.contrib.auth.models import User

booking_for_choice = (
    ('Rooms', 'Rooms'),
    ('Party Hall', 'Party Hall')
)

room_type_choice = (
    ('Luxury', 'Luxury'),
    ('Indoor', 'Indoor'),
    ("Single", 'Single'),
    ('double', 'double')
)

hall_type_choice = (
    ('Indoor', 'Indoor'),
    ('Indoor and Dining', 'Indoor and Dining'),
    ('Outdoor', 'Outdoor'),
    ('Out door and Dining', 'Out door and Dining')
)

booking_status_choice = (
    ('Open', 'Open'),
    ('Closed', 'Closed'),
    ('Cancelled', 'Cancelled')
)

payment_status_choice = (
    ('Complete', 'Complete'),
    ('Partial', 'Partial'),
    ('Nill', 'Nill')
)

mode_of_payment_choice = (
    ('Card', 'Card'),
    ('Gpay', 'Gpay'),
    ('Cash', 'Cash'),
    ('Net Transfer', 'Net Transfer')
)

payment_type_choice = (
    ('Credit', 'Credit'),
    ('Debit', 'Debit')
)


class Room_Type(models.Model):
    room_type = models.CharField(choices=room_type_choice, max_length=20)

    def __str__(self):
        return self.room_type


class Booking_Person_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=20, blank=False)
    mobile_no = models.CharField(max_length=10)
    adhaar_no = models.CharField(max_length=12)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Property_Details(models.Model):
    property_id = models.CharField(max_length=20, blank=False)
    name = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.name


class Booking_status(models.Model):
    booking_status = models.CharField(max_length=20, choices=booking_status_choice)

    def __str__(self):
        return self.booking_status


class Room_Booking_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    booking_id = models.CharField(max_length=20)
    oyo_booking_id = models.IntegerField(blank=True)
    room_type = models.ForeignKey(Room_Type, on_delete=models.PROTECT)
    no_of_rooms = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    def __str__(self):
        return self.booking_id


class Booking_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    booking_id = models.ForeignKey(Room_Booking_Details, on_delete=models.PROTECT)
    booking_date_time = models.DateTimeField(auto_now=True)
    booking_amount = models.IntegerField()
    booking_advance_amount = models.IntegerField()
    booking_status = models.ForeignKey(Booking_status, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username


class Hall_Type(models.Model):
    hall_type = models.CharField(choices=hall_type_choice, max_length=20)

    def __str__(self):
        return self.hall_type


class Room_Details(models.Model):
    room_property_id = models.ForeignKey(Property_Details, on_delete=models.PROTECT)
    room_no = models.IntegerField()
    room_type = models.ForeignKey(Room_Type, on_delete=models.PROTECT)

    def __str__(self):
        return self.room_property_id.name


class Payment_Status(models.Model):
    payment_status = models.CharField(max_length=10, choices=payment_status_choice)

    def __str__(self):
        return self.payment_status


class Room_Occupancy_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    booking_id = models.ForeignKey(Room_Booking_Details, on_delete=models.PROTECT)
    room_id = models.ForeignKey(Room_Details, on_delete=models.PROTECT)

    def __str__(self):
        return self.user.username


class Party_Hall_Booking_Details(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    booking_id = models.CharField(max_length=20)
    date_and_time = models.DateTimeField(auto_now=True)
    advance_amount = models.IntegerField()
    hall_type = models.ForeignKey(Hall_Type, on_delete=models.PROTECT)
    rent_amount = models.IntegerField()
    function_date = models.DateField()
    function_time = models.TimeField()
    refered_by = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.booking_id


class Mode_of_Payment(models.Model):
    mode_of_payment = models.CharField(max_length=30, choices=mode_of_payment_choice)

    def __str__(self):
        return self.mode_of_payment


class Payment_Type(models.Model):
    payment_type = models.CharField(max_length=10, choices=payment_type_choice)

    def __str__(self):
        return self.payment_type


class Room_Payment_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    payment_id = models.CharField(max_length=20, blank=False)
    amount = models.IntegerField()
    mode_of_payment = models.ForeignKey(Mode_of_Payment, on_delete=models.PROTECT)
    payment_type = models.ForeignKey(Payment_Type, on_delete=models.PROTECT)
    date_time = models.DateTimeField()
    booking_id = models.ForeignKey(Room_Booking_Details, on_delete=models.PROTECT)

    def __str__(self):
        return self.payment_id


class Party_Hall_Payment_details(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    payment_id = models.CharField(max_length=20, blank=False)
    amount = models.IntegerField()
    mode_of_payment = models.ForeignKey(Mode_of_Payment, on_delete=models.PROTECT)
    payment_type = models.ForeignKey(Payment_Type, on_delete=models.PROTECT)
    date_time = models.DateTimeField()
    booking_id = models.ForeignKey(Party_Hall_Booking_Details, on_delete=models.PROTECT)

    def __str__(self):
        return self.payment_id
