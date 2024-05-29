from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('',views.index, name='index'),
    path('destination/', views.destinations, name='destination'),
    path('viator/', views.viator, name='viator'),
    path('terms/',views.terms, name="terms"),
    path('privacy/',views.privacy, name="privacy"),
    path('refund/',views.refund, name="refund"),
    path('about/',views.about, name="about"),
    path('booking/',views.book_tour, name="booking"),
    path('booking/success/',views.booking_success, name="booking_success"),
    path('subscribe/success/',views.subscribe_success, name="subscribe_success"),
    path('subscribe/',views.subscribe, name="subscribe"),
    path('contact/',views.contact, name="contact"),
    path('packages/',views.packages, name="packages"),
    path('packages/detail/<int:tour_id>/', views.packages_detail, name='packages_detail'),
    
]
