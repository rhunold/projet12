from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter

from .overrides import AddGetDjangoModelPermissions
from .models import Employee, Client, Contract, Event

from .serializers import *


class EmployeeViewset(ModelViewSet):
    permission_classes = [AddGetDjangoModelPermissions]
    
    filter_backends = [SearchFilter]    
    search_fields = ['first_name', 'last_name', 'email', 'department']    

    def get_serializer_class(self):
        if self.action == 'list':
            return EmployeeListSerializer
        return EmployeeDetailSerializer

    def get_queryset(self):

        # Exclude the admin user        
        queryset = Employee.objects.exclude(id=1)

        # user = Employee.objects.get(id=self.request.user.id)

        return queryset


class ClientViewset(ModelViewSet):
    permission_classes = [AddGetDjangoModelPermissions]

    filter_backends = [SearchFilter]    
    search_fields = ['company_name', 'last_name', 'email']

    def get_serializer_class(self):
        if self.action == 'list':
            return ClientListSerializer
        return ClientDetailSerializer


    def get_queryset(self):
        queryset = Client.objects.all()

        user = Employee.objects.get(id=self.request.user.id)

        sales_employees = Employee.objects.filter(department="SALES")
        support_employees = Employee.objects.filter(department="SUPPORT")
           
        if user in sales_employees:
            queryset = Client.objects.filter(sales_contact=user)
        elif user in support_employees:
            support_employee_contrats = Event.objects.filter(support_contact=user).values_list('contrat', flat=True)
            support_employee_clients = Client.objects.filter(id__in=support_employee_contrats)
            queryset = Client.objects.filter(id__in=support_employee_clients)
        return queryset

  
class ContractViewset(ModelViewSet):
    permission_classes = [AddGetDjangoModelPermissions]

    filter_backends = [SearchFilter]
    search_fields = ['client__company_name', 'client__last_name', 'client__email', 'creation_date', 'amount']

    def get_serializer_class(self):
        if self.action == 'list':
            return ContractListSerializer
        return ContractDetailSerializer

    def get_queryset(self):
        queryset = Contract.objects.all()
        user = Employee.objects.get(id=self.request.user.id)
        sales_employees = Employee.objects.filter(department="SALES")

        if user in sales_employees:
            sales_contact_clients = Contract.objects.filter(sales_contact=user)
            queryset = Contract.objects.filter(id__in=sales_contact_clients)
        return queryset


class EventViewset(ModelViewSet):
    permission_classes = [AddGetDjangoModelPermissions]

    filter_backends = [SearchFilter]
    search_fields = ['contrat__client__company_name', 'contrat__client__last_name', 'contrat__client__email', 'event_date']

    def get_serializer_class(self):
        if self.action == 'list':
            return EventListSerializer
        return EventDetailSerializer

    def get_queryset(self):
        queryset = Event.objects.all()
        user = Employee.objects.get(id=self.request.user.id)

        support_employees = Employee.objects.filter(department="SUPPORT")
        if user in support_employees:
            support_contact_clients = Event.objects.filter(support_contact=user)
            queryset = Event.objects.filter(id__in=support_contact_clients)

        return queryset


# def test_error(request):
#     try:
#         1/0
#     except ZeroDivisionError:
#         return logging.exception("message")
