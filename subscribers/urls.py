from django.urls import path

from . import views

app_name = 'subscribers'

urlpatterns = [
    path('', views.SubscriberAPIView.as_view(), name='subscriber'),
]
