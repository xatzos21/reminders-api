from django.urls import path
from .views import (
    home,
    ReminderList,
    ReminderCreate,
    ReminderGetUpdateDestroy,
    UserList,
    UserDetail,
)
from .swagger import schema_view

urlpatterns = [
    path("", home, name="reminder-list"),
    path("api/v1/reminders/", ReminderList.as_view()),
    path("api/v1/reminders/create/", ReminderCreate.as_view()),
    path("api/v1/reminders/<int:pk>/", ReminderGetUpdateDestroy.as_view()),
    path("api/v1/users/", UserList.as_view()),
    path("api/v1/users/<int:pk>/", UserDetail.as_view()),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
]