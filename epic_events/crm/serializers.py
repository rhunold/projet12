from django.contrib.auth.hashers import make_password
from django.core import serializers
from rest_framework.serializers import ModelSerializer, ValidationError, SerializerMethodField, StringRelatedField, EmailField, RelatedField, DateTimeField
from .models import Employee, Client, Contract, Event
from django.db.models import Q


class EmployeeSerializer(ModelSerializer):
    # username = EmailField()
    
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'email', 'department']
        read_only = ['id', 'creation_date', 'modified_date']


class AssignedEmployee(RelatedField):
    def display_value(self, instance):
        return instance
    
    def to_representation(self, value):
        return str(value)
    
    def to_internal_value(self, data):
        try:
            employee = Employee.objects.get(id=data)
        except Employee.DoesNotExist:
            raise ValidationError('Employee does not exist.')
        except ValueError:
            raise ValidationError('id must be an integer.')
        
        sales_peoples = Employee.objects.filter(department="SALES")
        # support_peoples = Employee.objects.filter(department="SUPPORT")
        
        if employee not in sales_peoples:
            raise ValidationError(f'{employee.first_name} {employee.last_name} is not a sales personn')
        return employee
        

class ClientDetailSerializer(ModelSerializer): 
    sales_contact = AssignedEmployee(
        queryset=Employee.objects.all(), required=False
    )

    class Meta:
        model = Client
        fields = "__all__"
        read_only = ['id', 'creation_date', 'modified_date']
        # depth = 2



class ClientListSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"        
        # fields = ['id', 'company_name', 'client_statut', 'sales_contact']
        read_only = ['id', 'creation_date', 'modified_date']  
        
        
class ContractDetailSerializer(ModelSerializer):
    sales_contact = AssignedEmployee(
        queryset=Employee.objects.all(), required=False
    )
    
    payment_due = DateTimeField(input_formats=['%d-%m-%Y %H:%M',])

    class Meta:
        model =  Contract
        fields = "__all__"
        read_only = ['id', 'creation_date', 'modified_date']
        # depth = 2



class ContractListSerializer(ModelSerializer):        
    class Meta:
        model =  Contract
        fields = "__all__"        
        # fields = ['id', 'company_name', 'client_statut', 'sales_contact']
        read_only = ['id', 'creation_date', 'modified_date']
        
        
class EventDetailSerializer(ModelSerializer):
    # sales_contact = AssignedEmployee(
    #     queryset=Employee.objects.all(), required=False
    # )
    
    event_date = DateTimeField(input_formats=['%d-%m-%Y %H:%M',])

    class Meta:
        model =  Event
        fields = "__all__"
        read_only = ['id', 'creation_date', 'modified_date']
        # depth = 2



class EventListSerializer(ModelSerializer):        
    class Meta:
        model =  Event
        fields = "__all__"
        read_only = ['id', 'creation_date', 'modified_date']         
