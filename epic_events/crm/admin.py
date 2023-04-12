from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib.admin import ModelAdmin 
from .models import Employee, Client, Contract, Event


@admin.register(Client)
class ClientAdmin(ModelAdmin):
    list_display = ('company_name', 'first_name', 'last_name', 'client_statut', 'sales_contact')
    search_fields = ('company_name', 'email')
    readonly_fields = [
        'creation_date',
        'modified_date',
    ]        
    
    # Only show Sales Employee in select form
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sales_contact":
            kwargs["queryset"] = Employee.objects.filter(department__in=['SALES'])
            
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

 

@admin.register(Contract)
class ContractAdmin(ModelAdmin):
    list_display = ('__str__', 'client', 'amount', 'payment_due', 'creation_date', 'contrat_statut')
    search_fields = [
        'client__email',
        'client__company_name',
        'client__first_name',
        'client__last_name',
        'sales_contact__last_name',
        'sales_contact__first_name'
        ]
    readonly_fields = [
        'creation_date',
        'modified_date',
    ]    
    
    # Only show Sales Employee in select form and for clients, do not show prospects
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "sales_contact":
            kwargs["queryset"] = Employee.objects.filter(department__in=['SALES'])
        if db_field.name == "client":
            kwargs["queryset"] = Client.objects.filter(client_statut=True)
        return super().formfield_for_foreignkey(db_field, request, **kwargs)    
    
@admin.register(Event)
class EventAdmin(ModelAdmin):
    list_display = ('__str__', 'get_client', 'event_statut', 'attendees', 'event_date', 'support_contact')
    search_fields = [
        'contrat__client__email',
        'contrat__client__company_name',
        'contrat__client__first_name',
        'contrat__client__last_name',    
        'support_contact__last_name',
        'support_contact__first_name',
        'notes'
        ]
    readonly_fields = [
        'creation_date',
        'modified_date',
    ]
    

    # Only show Support Employee in select form and only contract signed.
    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "support_contact":
            kwargs["queryset"] = Employee.objects.filter(department__in=['SUPPORT'])
        if db_field.name == "contrat":
            kwargs["queryset"] = Contract.objects.filter(contrat_statut=True)

        return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    @admin.display(ordering='client__company_name', description='Client')
    def get_client(self, obj):
        return obj.contrat.client
  

    
@admin.register(Employee)
class EmployeeAdmin(UserAdmin):
    """Define admin model for custom User model with no email field."""

    add_fieldsets = (
        (None, {
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'department', 'creation_date', 'modified_date')
    search_fields = ('email', 'first_name', 'last_name', 'department')
    ordering = ('email',)
    
    readonly_fields = [
        'creation_date',
        'modified_date',
        'last_login',
        'date_joined',
    ]
    
    list_filter = ("email", "is_staff", "is_active",)    

    
    # Get fields depending if superuser or manager
    def get_fieldsets(self, request, obj=None):
        if not obj:
            return self.add_fieldsets

        if request.user.is_superuser:
            perm_fields = ('is_active', 'is_staff', 'is_superuser',
                            'groups', 'user_permissions', )
            
        else:
            # modify these to suit the fields you want the managers users to be able to edit
            perm_fields = ('is_active', 'groups',)
            

        return [
            (None, {'fields': ('email', 'password')}),
                (('Personal info'), {'fields': ('first_name', 'last_name',)}),
                (('Permissions'), {'fields': perm_fields}),
                ('Dates', {'fields': ('creation_date', 'modified_date',)}), 
                ('Departement', {'fields': ('department',)}),                 
                ]
    
    
    def get_queryset(self, request):
        qs = super(UserAdmin, self).get_queryset(request)
        if not request.user.is_superuser:
            # Don't show super user in the list of users
            qs = qs.filter(is_superuser=False)
            # Don't show other Managers but every other employees
            qs = qs.filter(pk=request.user.id) | qs.filter(department='SALES') | qs.filter(department='SUPPORT') | qs.filter(department=None) 
            return qs 
        return qs
    
   
    
    def has_delete_permission(self, request, obj=None):
        if request.user.is_superuser:
            return True
        elif request.user == obj:
            return True
        elif request.user.groups.filter(name="Manager").exists():
            return True
        else:
            # Can't delete superuser (with pk=1) when viewing profil
            return obj is None or obj.pk != 1  

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()

        if not is_superuser: 
            disabled_fields = {
                'is_superuser',
                'user_permissions',
                'is_staff',          
            }
            
        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True
        return form
    
