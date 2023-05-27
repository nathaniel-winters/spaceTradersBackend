from django.urls import path
from . import views

urlpatterns = [
    path('agent/', views.get_agent)
]