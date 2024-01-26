from django.urls import path
from .views import signup, log_in, log_out, profile

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('profile/<str:id>', profile, name='profile')
]
