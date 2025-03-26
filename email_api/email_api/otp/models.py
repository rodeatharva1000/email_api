from django.db import models


class OTP(models.Model):
    email = models.EmailField(unique=True)
    code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)
    is_verified = models.BooleanField(default=False)

    class Meta:
        verbose_name = "OTP Code"
        verbose_name_plural = "OTP Codes"

    def __str__(self):
        return f"{self.email[:5]}... - {self.code}"
