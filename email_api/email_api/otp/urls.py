from django.urls import path
from .views import SendOTPAPI

app_name = 'otp'

urlpatterns = [
    path('send-otp/', SendOTPAPI.as_view(), name='send_otp'),
]
