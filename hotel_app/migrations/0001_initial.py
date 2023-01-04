# Generated by Django 4.1.5 on 2023-01-04 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking_Person_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mobile_no', models.IntegerField()),
                ('adhaar_no', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Booking_status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed'), ('Cancelled', 'Cancelled')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Hall_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hall_type', models.CharField(choices=[('Indoor', 'Indoor'), ('Indoor and Dining', 'Indoor and Dining'), ('Outdoor', 'Outdoor'), ('Out door and Dining', 'Out door and Dining')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Mode_of_Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mode_of_payment', models.CharField(choices=[('Card', 'Card'), ('Gpay', 'Gpay'), ('Cash', 'Cash'), ('Net Transfer', 'Net Transfer')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Party_hall_Booking_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(max_length=20)),
                ('date_and_time', models.DateTimeField(auto_now=True)),
                ('advance_amount', models.IntegerField()),
                ('rent_amount', models.IntegerField()),
                ('function_date', models.DateField()),
                ('function_time', models.TimeField()),
                ('refered_by', models.CharField(blank=True, max_length=20)),
                ('hall_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_app.hall_type')),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_status', models.CharField(choices=[('Complete', 'Complete'), ('Partial', 'Partial'), ('Nill', 'Nill')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Payment_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_type', models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Property_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=20)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Room_Booking_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.CharField(max_length=20)),
                ('oyo_booking_id', models.IntegerField(blank=True)),
                ('no_of_rooms', models.IntegerField()),
                ('from_date', models.DateField()),
                ('to_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Room_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.IntegerField()),
                ('room_property_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_app.property_details')),
            ],
        ),
        migrations.CreateModel(
            name='Room_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_type', models.CharField(choices=[('Luxury', 'Luxury'), ('Indoor', 'Indoor'), ('Single', 'Single'), ('double', 'double')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Room_Payment_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.CharField(max_length=20)),
                ('amount', models.IntegerField()),
                ('date_time', models.DateTimeField()),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_app.room_booking_details')),
                ('mode_of_payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_app.mode_of_payment')),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_app.payment_type')),
            ],
        ),
        migrations.CreateModel(
            name='Room_Occupancy_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_app.room_booking_details')),
                ('room_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_app.room_details')),
            ],
        ),
        migrations.AddField(
            model_name='room_details',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_app.room_type'),
        ),
        migrations.AddField(
            model_name='room_booking_details',
            name='room_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_app.room_type'),
        ),
        migrations.CreateModel(
            name='Party_Hall_Payment_details',
            fields=[
                ('payment_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.IntegerField()),
                ('date_time', models.DateTimeField()),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_app.party_hall_booking_details')),
                ('mode_of_payment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_app.mode_of_payment')),
                ('payment_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_app.payment_type')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CheckOut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_out_date', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel_app.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Booking_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date_time', models.DateTimeField(auto_now=True)),
                ('booking_amount', models.IntegerField()),
                ('booking_advance_amount', models.IntegerField()),
                ('booking_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_app.booking_details')),
                ('booking_status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='hotel_app.booking_status')),
            ],
        ),
    ]
