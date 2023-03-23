from django.urls import path
from forapp import views
urlpatterns = [
    path("for/",views.forvw),
    path("for1/",views.for1),
    path("filter/",views.filtervw),
]