from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('countries/', views.countries, name="countries"),
    path('<country>', views.numbers, name="numbers"),
    path('<country>/<number>', views.messages, name="messages"),
]
