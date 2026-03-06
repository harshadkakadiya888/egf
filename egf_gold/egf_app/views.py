from rest_framework import generics
from .models import Address
from django.shortcuts import render
from .serializers import AddressSerializer
from django.http import HttpResponse
from rest_framework.parsers import MultiPartParser, FormParser

class AddressListCreateView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class AddressDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


def form_page(request):
    return render(request, "form.html")

def home(request):
    return HttpResponse("Welcome to the Address API!")


class AddressListCreateView(generics.ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    parser_classes = (MultiPartParser, FormParser)