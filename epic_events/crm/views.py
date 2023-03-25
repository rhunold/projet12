from rest_framework.viewsets import ModelViewSet

from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from rest_framework.permissions import AllowAny, DjangoModelPermissions # , IsAuthenticated, 

from rest_framework.exceptions import APIException, ValidationError

from .models import Employee, Client, Contract, Event

from .serializers import (
    # EmployeeSerializer,
    # ClientSerializer,    
    ClientListSerializer, ClientDetailSerializer,
    ContractListSerializer, ContractDetailSerializer,
    EventListSerializer, EventDetailSerializer,    
    )


# class SignUpView(ModelViewSet):
#     permission_classes = [AllowAny]
#     serializer_class = EmployeeSerializer

class AddGetDjangoModelPermissions(DjangoModelPermissions):
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']



class ClientViewset(ModelViewSet):
    permission_classes = [AddGetDjangoModelPermissions]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ClientListSerializer
        return ClientDetailSerializer

    def get_queryset(self):
        user = self.request.user
        print(user.id)
        print(user)
        
        queryset = Client.objects.all()
        return queryset
    
  


  
class ContractViewset(ModelViewSet):
    permission_classes = [AddGetDjangoModelPermissions]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ContractListSerializer
        return ContractDetailSerializer

    def get_queryset(self):
        user = self.request.user
        print(user.id)
        print(user)        

        queryset = Contract.objects.all()
        return queryset


class EventViewset(ModelViewSet):
    permission_classes = [AddGetDjangoModelPermissions]
    
    def get_serializer_class(self):
        if self.action == 'list':
            return EventListSerializer
        return EventDetailSerializer

    def get_queryset(self):
        user = self.request.user
        print(user.id)
        print(user)        

        queryset = Event.objects.all()
        return queryset
