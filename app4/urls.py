from django.urls import path
from app4 import views

urlpatterns = [
                path('about/<n>/<x>/',views.about)
]