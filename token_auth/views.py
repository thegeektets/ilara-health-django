from django.contrib.auth import authenticate, login
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Token


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    user = authenticate(request, email=email, password=password)

    print(user)

    if user is not None:
        # login(request._request, user)
        # generate and return the token
        token, created = Token.objects.get_or_create(user=user)

        print(token)
        return Response({'token': token.key})
    else:
        return Response({'error': 'Invalid credentials'}, status=400)
