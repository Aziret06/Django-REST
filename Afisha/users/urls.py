from django.urls import path
from . import views

urlpatterns = [
    path('registration/', views.RegistrationAPIView.as_view()),
    path('authorization/', views.LoginAPIView.as_view()),
    path('confirm_sms/', views.ConfirmSMSAPIView.as_view()),
]