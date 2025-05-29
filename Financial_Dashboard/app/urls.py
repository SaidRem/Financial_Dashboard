from django.urls import path
from .views import current_time, workdir, index

urlpatterns = [
    path('', index),
    path('curtime/', current_time),
    path('workdir/', workdir)
]