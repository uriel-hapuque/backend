from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView
from users.views import ListCreateUserView, RetrieveUpdateDestroyUserView

urlpatterns = [
    path('users/', ListCreateUserView.as_view()),
    path('users/<int:user_id>/', RetrieveUpdateDestroyUserView.as_view()),
    path('login/', TokenObtainPairView.as_view())
]
