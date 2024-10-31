from custom_types.serializers import Custom_TypeSerializer
from custom_types.models import Custom_Type
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from custom_types.permissions import IsCustom_TypeCreator, ReadOnly

class ListCreateCustom_TypeView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Custom_Type.objects.all()
    serializer_class = Custom_TypeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class RetrieveUpdateDestroyCustom_TypeView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCustom_TypeCreator | ReadOnly]
    queryset=Custom_Type.objects.all()
    serializer_class=Custom_TypeSerializer
    lookup_url_kwarg='type_id'

