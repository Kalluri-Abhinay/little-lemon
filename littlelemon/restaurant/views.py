from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from .models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer

# Handles GET (list all) and POST (create new)
class MenuItemsView(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

# Handles GET (retrieve one), PUT (update), DELETE (delete)
class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]


def index(request):
   return render(request, 'index.html', {})