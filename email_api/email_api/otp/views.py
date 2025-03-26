import random
from django.core.mail import send_mail
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class SendOTPAPI(APIView):
    def post(self, request):
        email = request.data.get('email')

        if not email:
            return Response(
                {"error": "Email is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Generate a 6-digit OTP
        otp = str(random.randint(100000, 999999))

        # Send OTP via email
        send_mail(
            'Your OTP Code',
            f'Your verification code of Farmer Equipment Rental Service Platform is: {otp}',
            None,  # Uses DEFAULT_FROM_EMAIL from settings.py
            [email],
            fail_silently=False,
        )

        return Response({
            "status": "success",
            "message": "OTP sent successfully",
            "otp": otp  # Sending OTP in response (only for testing)
        }, status=status.HTTP_200_OK)
