from django.urls import path
from . import views
urlpatterns = [
    path('', views.ClintSysView.as_view())
]
