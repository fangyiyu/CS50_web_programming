# The ability to reroute URLs 
from django.urls import path
# Import any functions created in views.py
from . import views

urlpatterns = [
    path("", views.index1, name="index"),
    path("<str:name>", views.greet1, name="greet"),
    path("brian", views.brian, name="brian"),
    path("david", views.david, name="david"),
]
