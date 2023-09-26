from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='user_signup'),
    path('login/', views.LoginView.as_view(), name='user_login'),
]
