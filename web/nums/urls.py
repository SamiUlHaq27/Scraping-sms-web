from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('countries/', views.countries, name="countries"),
    path('country/<country>', views.numbers, name="numbers"),
    path('country/<country>/number/<number>', views.messages, name="messages"),
    path('about/', views.about, name="about"),
    # path('run/', views.run, name="run"),
]
