from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import User
from api.serializers import SignupSerializer


@api_view(["POST"])
def send_confirmation_code(request):
    if request.method == "POST":
        serializer = SignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data.get('email')
        user, _ = User.objects.get_or_create(email=email)
        token = default_token_generator.make_token(user)
        send_mail(
            subject="Your confirmation code is inside!",
            message=f"Please use this code: {str(token)} to login and use API",
            from_email="support@yamdb.com",
            recipient_list=[email],
        )
        return Response("Confirmation code is sent to your email.")
