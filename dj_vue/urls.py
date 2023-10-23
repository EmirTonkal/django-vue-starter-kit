
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path("", include("todos.urls")),
    path("admin/", admin.site.urls),
    path("api/", include("todos.urls")),
]
