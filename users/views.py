from users.serializers import UserSerializer
from users.models import User
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class ListCreateUserView(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class RetrieveUpdateDestroyUserView(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg="user_id"