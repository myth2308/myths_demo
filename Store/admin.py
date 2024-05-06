from django.contrib import admin
from . import models
from .models import Tour, Booking, Packages, Subscriber, DestinationImage, PackageImage,Contact
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget


admin.site.register(models.Destination)
admin.site.register(models.Carousel)
admin.site.register(models.Terms)



@admin.register(PackageImage)
class PackageImageAdmin(admin.ModelAdmin):
    
    list_per_page = 20

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone_number','message','subject','contact_at',]
    list_per_page = 20

@admin.register(DestinationImage)
class DestinationImageAdmin(admin.ModelAdmin):
    list_per_page = 20


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display = ['email','subscriber_at',]
    list_per_page = 20


class PackagesForm(forms.ModelForm):
    
    content = forms.CharField(widget=CKEditorUploadingWidget())
    
    class Meta:
        model = Packages
        fields = '__all__'


@admin.register(Packages)
class PackagesAdmin(admin.ModelAdmin):
    list_display = ['destination_name','duration_date','price','price_old',]
    form = PackagesForm  # Sử dụng PackagesForm
    list_per_page = 20
    search_fields = ['duration_date','destination_name__istartswith',]


@admin.register(Tour)
class TourAdmin(admin.ModelAdmin):
    list_display = ['id', 'destination', 'departure_date']
    list_filter = ['departure_date',]
    list_per_page = 20
    search_fields = ['destination__istartswith']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['id', 'tour', 'name', 'email', 'phone_number', 'adults', 'children', 'special_requests','booking_at']
    list_filter = ['tour', 'name', 'email', 'phone_number']
    search_fields = ['name', 'email', 'phone_number']
    list_per_page = 20