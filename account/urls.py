from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='user_signup'),
    path('login/', views.LoginView.as_view(), name='user_login'),
    path('profile/', views.ProfileView.as_view(), name='user_edit_profile'),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name='user_show_profile'),
]
