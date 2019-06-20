from django.urls import path
from . import views
urlpatterns = [
    path('v1/feeder/', views.main,name='main')
]