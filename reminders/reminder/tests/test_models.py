from django.test import TestCase
from ..models import Reminder
from django.contrib.auth.models import User
import datetime


class ReminderTest(TestCase):
    def setUp(self):
        user1 = User.objects.create_user(username="user1")
        user2 = User.objects.create_user(username="user2")
        Reminder.objects.create(
            title="omadara",
            description="megalyteri omada",
            due_date=datetime.date.today(),
            user=user1,
        )
        Reminder.objects.create(
            title="omadara1",
            description="megalyteri omada1",
            due_date=datetime.date.today(),
            user=user2,
        )

    def test_reminder_title(self):
        reminder_omadara = Reminder.objects.get(title="omadara")
        reminder_omadara1 = Reminder.objects.get(title="omadara1")
        self.assertEqual(
            reminder_omadara.get_title(), "Name of the reminder is: omadara"
        )
        self.assertEqual(
            reminder_omadara1.get_title(), "Name of the reminder is: omadara1"
        )