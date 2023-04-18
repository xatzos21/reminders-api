from rest_framework.test import APITestCase
from reminder.models import Reminder
from django.contrib.auth.models import User

reminder_schema = {
    "title": "omadara",
    "description": "megalyteri omada",
    "due_date": "2023-02-22",
}

user1_schema = {
    "username": "admin",
    "email": "admin@admin.com",
    "password": "admin",
}


class ReminderListTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(**user1_schema)
        reminder_schema["user"] = self.user1
        Reminder.objects.create(**reminder_schema)

    def test_list_reminders(self):
        reminder_count = Reminder.objects.count()
        response = self.client.get("/api/v1/reminders/")
        self.assertIsNone(response.data["next"])
        self.assertIsNone(response.data["previous"])
        self.assertEqual(reminder_count, response.data["count"])
        self.assertEqual(reminder_count, len(response.data["results"]))


class ReminderCreateTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(**user1_schema)

    def test_create_reminder(self):
        initial_count = Reminder.objects.count()

        reminder_data = reminder_schema.copy()
        reminder_data["user"] = self.user1.pk

        response = self.client.post("/api/v1/reminders/create/", reminder_data)
        self.assertEqual(Reminder.objects.count(), initial_count + 1)

        for attr, value in reminder_schema.items():
            self.assertEqual(response.data[attr], value)


class ReminderUpdateTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(**user1_schema)
        reminder_schema["user"] = self.user1
        self.reminder = Reminder.objects.create(**reminder_schema)

    def test_update_reminder(self):
        reminder_title = "omadara"
        self.assertEqual(self.reminder.title, reminder_schema["title"])

        reminder_data = reminder_schema.copy()
        reminder_data["title"] = reminder_title
        reminder_data["user"] = self.user1.pk

        response = self.client.patch(
            f"/api/v1/reminders/{self.reminder.id}/",
            reminder_data,
            format="json",
        )
        updated_reminder = Reminder.objects.get(id=self.reminder.id)
        self.assertEqual(updated_reminder.title, reminder_title)
        self.assertEqual(response.data["title"], reminder_title)


class ReminderDeleteTest(APITestCase):
    def setUp(self):
        self.user1 = User.objects.create_user(**user1_schema)
        self.reminder = Reminder.objects.create(user=self.user1, **reminder_schema)

    def test_delete(self):
        initial_count = Reminder.objects.count()
        response = self.client.delete(f"/api/v1/reminders/{self.reminder.id}/")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(initial_count - 1, Reminder.objects.count())
