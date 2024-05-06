from django.db import models
from django.template.defaultfilters import slugify
from ckeditor.fields import RichTextField
from django.contrib.staticfiles.handlers import StaticFilesHandler
# Create your models here.


class Carousel(models.Model):

    image = models.ImageField(upload_to='carousel_img/')
    

    def __str__(self):
        return f"Carousel Image: {self.image.name}"

class Destination(models.Model):
    
    country = models.CharField(max_length=100,null=True,blank=True)

    def __str__(self):
        return self.country


class DestinationImage(models.Model):
    destination = models.ForeignKey(Destination, related_name='images', on_delete=models.CASCADE)
    name = models.CharField(max_length=100,blank=True,null=True)
    image = models.ImageField(upload_to='destination_images/')

    def __str__(self):
        return self.destination.country



class Packages(models.Model):
    destination_name = models.CharField(max_length=100) # Tên nơi du lịch
    duration_days = models.CharField(max_length=100) #Số ngày
    duration_date = models.CharField(max_length=100) #ngay khoi hanh
    price = models.CharField(max_length=100) #Giá
    price_old = models.CharField(max_length=100,null=True,blank=True) #Giá
    num_person = models.IntegerField()
    image = models.ImageField(upload_to='packages_img/') #Hình ảnh
    content = RichTextField(null=True, blank=True)
    viewed = models.IntegerField(default=0)
    read_more_url = models.URLField(max_length=200, blank=True, null=True)


    def __str__(self):
        return self.destination_name

class PackageImage(models.Model):
    package = models.ForeignKey(Packages, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='packages_img/') #Hình ảnh

    def __str__(self):
        return f"Image for {self.package.destination_name}"

class Contact(models.Model):
    name = models.CharField(max_length=150,)
    phone_number = models.CharField(max_length=15, default='')
    email = models.EmailField()
    subject = models.CharField(max_length=20, null=True)
    message = models.TextField()
    contact_at = models.DateTimeField(auto_now_add=True,null=True)


    def __str__(self):
        return self.name
    
class Tour(models.Model):
    destination = models.CharField(max_length=100)
    departure_date = models.DateField()


    def __str__(self):
        return self.destination
    
class Booking(models.Model):
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    adults = models.IntegerField(default=1)
    children = models.IntegerField(default=0)
    special_requests = models.TextField(null=True, blank=True)
    booking_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f"{self.name} - {self.tour.destination}"
    
class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    subscriber_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    

class Terms(models.Model):
    content = RichTextField(null=True,blank=True)