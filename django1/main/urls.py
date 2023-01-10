from django.urls import path

# Import "views.py" file from current folder
from . import views

urlpatterns = [
	path("<int:id>", views.index, name="index"),
	path("", views.home, name="home"),
	path("create/", views.create, name="create"),
]