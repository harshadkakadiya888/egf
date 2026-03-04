from django.urls import path
from .views import AddressListCreateView, AddressDetailView, form_page

urlpatterns = [
    path('addresses/', AddressListCreateView.as_view()),
    path('addresses/<int:pk>/', AddressDetailView.as_view()),
    path('form/', form_page, name='form_page'),
]
