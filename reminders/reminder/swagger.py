from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny

schema_view = get_schema_view(
    openapi.Info(
        title="Reminder API",
        default_version="v1",
        description="An API about reminders",
        contact=openapi.Contact(email="contact@myapi.local"),
    ),
    public=True,
    permission_classes=[AllowAny],
)