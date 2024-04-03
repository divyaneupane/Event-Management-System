from django.db import models

# Create your models here.
class Event(models.Model):
    img=models.ImageField(upload_to="pic")
    name=models.CharField(max_length=100)
    desc=models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.name




class Booking(models.Model):
    cus_name=models.CharField(max_length=50)
    cus_phone=models.CharField(max_length=10)
    name=models.ForeignKey(Event,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booking_on=models.DateField(auto_now=True)