from django.urls import path
from app1 import views

urlpatterns = [
                path("ap1/",views.ap1),
                path('two/<int:pk>/<int:fk>/',views.two),
                path('about/<int:a>/<int:b>/',views.compare),
]