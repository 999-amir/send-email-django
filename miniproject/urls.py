from django.urls import path
from .views import EmailTestView

app_name = 'mini_project'

urlpatterns = [
    path('email/', EmailTestView.as_view(), name='email'),
]