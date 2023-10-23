from django.urls import path
from . import views
from rest_framework import routers
from todos.views import VueTodoTemplateView, TodoViewset


app_name = "todos"

router = routers.DefaultRouter()

router.register("todos", TodoViewset)

urlpatterns = [
    ##path("", views.home, name='home'),
    path("", VueTodoTemplateView.as_view(),name="todo_home"),
]

urlpatterns += router.urls