from django.urls import path
from .views import CreateAccountView, ProfileView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    # view user profile
    path('<int:pk>/', ProfileView.as_view(), name='profile'),
]
