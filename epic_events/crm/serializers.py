from rest_framework import serializers
from .models import Employee, Client, Contract, Event
from django.db.models import Q
from django.utils.translation import gettext_lazy as _

class EmployeeDetailSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Employee
        # fields = "__all__"        
        fields = ['id', 'first_name', 'last_name', 'email', 'department', 'creation_date', 'modified_date', 'password']
        read_only = ['id', 'creation_date', 'modified_date']
        extra_kwargs = {'password': {'write_only': True}}
        
    def create(self, validated_data):
        user = Employee.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            if key == 'password':
                instance.set_password(value)
            else:
                setattr(instance, key, value)
        instance.save()
        return instance    


class EmployeeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['id', 'first_name', 'last_name', 'department', 'email']


class ClientDetailSerializer(serializers.ModelSerializer):
    sales_contact = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.filter(department="SALES"),
        error_messages={'does_not_exist': _("Cet employé n'existe pas ou ne fait pas parti de l'équipe de vente"),
                        'incorrect_type': _("Vous devez mettre un chiffre."),},
        )

    class Meta:
        model = Client
        fields = "__all__"
        read_only = ['id', 'creation_date', 'modified_date']
        # depth = 1
        

class ClientListSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = Client
        fields = ['id', 'company_name', 'client_statut', 'sales_contact', 'email']
        read_only = ['id', 'creation_date', 'modified_date']  
        

        
class ContractDetailSerializer(serializers.ModelSerializer):
    sales_contact = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.filter(department="SALES"),
        error_messages={'does_not_exist': _("Cet employé n'existe pas ou ne fait pas parti de l'équipe de vente"),
                        'incorrect_type': _("Vous devez mettre un chiffre."),},
        )
    
    client = serializers.PrimaryKeyRelatedField(
        queryset=Client.objects.all(),
        error_messages={'does_not_exist': _("Ce client n'existe pas"),
                        'incorrect_type': _("Vous devez mettre un chiffre."),}, 
        )    
       
    payment_due = serializers.DateTimeField(input_formats=['%d-%m-%Y %H:%M',])

    class Meta:
        model =  Contract
        fields = "__all__"
        read_only = ['id', 'creation_date', 'modified_date']
        # depth = 1


class ContractListSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Contract     
        fields = ['id', 'client', 'contrat_statut', 'sales_contact']
        read_only = ['id', 'creation_date', 'modified_date']
    

      
class EventDetailSerializer(serializers.ModelSerializer):
    support_contact = serializers.PrimaryKeyRelatedField(
        queryset=Employee.objects.filter(department="SUPPORT"),
        error_messages={'does_not_exist': _("Cet employé n'existe pas ou ne fait pas parti de l'équipe support"),
                        'incorrect_type': _("Vous devez mettre un chiffre."),},
        )
    
    contrat = serializers.PrimaryKeyRelatedField(
        queryset=Contract.objects.filter(contrat_statut=True),
        error_messages={'does_not_exist': _("Ce contrat n'existe pas ou n'a pas été encore signé."),
                        'incorrect_type': _("Vous devez mettre un chiffre."),},
        )

    event_date = serializers.DateTimeField(input_formats=['%d-%m-%Y %H:%M',])

    class Meta:
        model =  Event
        fields = "__all__"
        read_only = ['id', 'creation_date', 'modified_date']


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model =  Event
        fields = ['id', 'contrat', 'support_contact']
        read_only = ['id', 'creation_date', 'modified_date']         
        # depth = 1
