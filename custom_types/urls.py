from django.urls import path
from custom_types.views import ListCreateCustom_TypeView, RetrieveUpdateDestroyCustom_TypeView

urlpatterns = [
    path('types/', ListCreateCustom_TypeView.as_view()),
    path('type/<int:type_id>/', RetrieveUpdateDestroyCustom_TypeView.as_view())
]
