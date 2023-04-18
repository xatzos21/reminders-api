from django.http import HttpResponse
from rest_framework import generics
from .models import Reminder
from django.contrib.auth.models import User
from .serializer import ReminderSerializer, UserSerializer
from rest_framework.pagination import LimitOffsetPagination


def home(request):
    return HttpResponse("home")


class PaginatedReminders(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10


class ReminderList(generics.ListAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer
    pagination_class = PaginatedReminders


class ReminderCreate(generics.CreateAPIView):
    serializer_class = ReminderSerializer


class ReminderGetUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer