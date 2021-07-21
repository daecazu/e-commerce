"""user views"""

# Django RF imports
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework import generics, authentication, permissions


# Django imports
from django.contrib.auth import authenticate

from django.contrib.auth import login
from django.contrib.auth import logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.shortcuts import redirect

# Exceptions
from django.db.utils import IntegrityError

# models and serializers
from user.serializers import AuthTokenSerializer
from user.serializers import UserSerializer

def login_view(request):
    """login view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/admin/')
        else:
            return render(
                request,
                'users/login.html',
                {'error': 'invalid username or password'}
            )
    return render(request, 'users/login.html')


@login_required
def logout_view(request):
    """logout view"""
    logout(request)
    return redirect("users:login")


def signup_view(request):
    """sign up view"""
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        password_confirmation = request.POST['password_confirmation']
        if password != password_confirmation:
            return render(
                request,
                'users/signup.html',
                {'error': 'password confirmation does not match'}
            )
        try:
            get_user_model().objects.create_user(
                email=email,
                password=password
            )
        except IntegrityError:
            return render(
                request,
                'users/signup.html',
                {'error': 'email already in use'}
            )

        return redirect("users:login")
    return render(request, 'users/signup.html')


class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer


class CreateTokenView(ObtainAuthToken):
    """Create a new token for a user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        """Retrieve and return authenticated user"""

        return self.request.user
