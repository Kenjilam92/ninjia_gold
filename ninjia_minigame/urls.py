from django.urls import path
from . import views
urlpatterns=[
    path ('',views.minigame),
    path ('process_money',views.process_money)
]