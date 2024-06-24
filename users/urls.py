from django.urls import path
from django.contrib.auth import views as auth_views
from . import views  # Import views module from current package (assuming views.py exists in the same directory)

app_name = 'users'

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),  # Use views.register here
    # other paths
]





