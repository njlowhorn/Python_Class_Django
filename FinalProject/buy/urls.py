from django.urls import path
from . import views

urlpatterns = [
    path("", views.buy, name="buy"),
    path("desktop", views.desktop, name="desktop"),
    path("laptop", views.laptop, name="laptop"),
    path("thanks", views.thanks, name="thanks")
]