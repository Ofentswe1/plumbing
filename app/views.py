from django.views import View
from django.contrib.auth.models import User
from django.core import serializers
from django.contrib.auth import authenticate, login
from django.http import HttpResponse


class Login(View):
    def get(self, request, *args, **kwargs):
        username = kwargs['username']
        password = kwargs['password']
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                username = user.username
                user = authenticate(username=username, password=password)
                login(request, user)
                details = User.objects.get(username=username)
                serialized_obj = serializers.serialize('json', [details, ])
                return HttpResponse(serialized_obj)
            else:
                return HttpResponse('{"messages":"Wrong password"}')
        except User.DoesNotExist:
            return HttpResponse(
                '{"message": "username and password incorrect"}')


class AllBookings(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('{"Success":"name"}')
