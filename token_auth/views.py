import datetime
from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Token
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, email=email, password=password)

    if user is not None:
        # generate and return the token
        token = Token.objects.get(user_id=user.id)

        if not token:
            # update the created time of the token to keep it valid
            created = datetime.datetime.now(datetime.timezone.utc)
            key = get_random_string(length=32)
     
            token = Token.objects.create(
            user=user, key=key, created=created)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid credentials'}, status=400)
