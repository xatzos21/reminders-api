from rest_framework import serializers
from .models import Reminder
from django.contrib.auth.models import User


class ReminderSerializer(serializers.ModelSerializer):
    class Meta:
        title = serializers.CharField(min_length=5, max_length=200)
        description = serializers.CharField(min_length=5, max_length=2000)
        user = serializers.ReadOnlyField(source="user.username")

        model = Reminder
        fields = ("id", "title", "description", "due_date", "user")


class UserSerializer(serializers.ModelSerializer):
    reminders = ReminderSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "reminders")