from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from .overrides import UserManager
from django.core.validators import RegexValidator


class DateMixin(models.Model):
    creation_date = models.DateTimeField(verbose_name='Creation date', auto_now_add=True, null=False, blank=True)
    modified_date = models.DateTimeField(verbose_name='Modified date', auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True

class Employee(DateMixin, AbstractUser):

    EMPLOYEE_TYPE = [
    ('SALES','SALES'),
    ('SUPPORT','SUPPORT'),
    ('MANAGER','MANAGER'),
    ]

    username = None
    email = models.EmailField(verbose_name='email address', max_length=100, unique=True, error_messages ={
                    "unique":"Cet email est déjà utilisé par un autre compte."
                    })
    password = models.CharField(verbose_name='password', max_length=100)

    first_name = models.CharField(verbose_name='first name', max_length=25)
    last_name = models.CharField(verbose_name='last name', max_length=25)

    department = models.CharField(verbose_name='department', max_length=20, choices=EMPLOYEE_TYPE, null=True, blank=True)    

    USERNAME_FIELD = 'email'    
    REQUIRED_FIELDS = []
    objects = UserManager()    

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = "Employé"
        verbose_name_plural = "Employés"
        ordering = ('-creation_date',)


class Client(DateMixin, models.Model):
    company_name = models.CharField(max_length=250, blank=False, default="No Company name")

    first_name = models.CharField(max_length=25, blank=False)
    last_name = models.CharField(max_length=25, blank=False)
    email = models.EmailField(max_length=100, unique=True)

    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Merci de mettre entre 9 et 12 chiffres.")
    phone = models.CharField(validators=[phone_regex], max_length=12, blank=True)
    mobile = models.CharField(validators=[phone_regex], max_length=12, blank=True)

    client_statut = models.BooleanField(verbose_name='Client', default=False,
                                        help_text="Laissez la checkbox vide s'il s'agit d'un prospect") 
    
    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.SET_NULL,
                                     null=True, blank=True, 
                                     related_name='client')    

    def __str__(self):
        return f"{self.company_name}"

    class Meta:
        verbose_name = "Client/Prospect"
        verbose_name_plural = "Clients/Prospects"
        ordering = ['company_name']


class Contract(DateMixin, models.Model):

    sales_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                     on_delete=models.SET_NULL,
                                     null=True, blank=True, 
                                    #  limit_choices_to={"department": "SALES"},
                                    #  error_messages = {'invalid_choice': "This id is not a Sales personn ID"},                                     
                                     related_name='contract')
    client = models.ForeignKey(Client, on_delete=models.CASCADE,
                               related_name='contract')

    contrat_statut = models.BooleanField(default=False,
                                        verbose_name='Contrat signé')
    amount = models.FloatField()
    payment_due = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Contrat n°{self.id} : {self.client.company_name}"

    class Meta:
        verbose_name = "Contrat"
        verbose_name_plural = "Contrats"

        
class Event(DateMixin, models.Model):
    contrat = models.ForeignKey(Contract, on_delete=models.SET_NULL,
                                null=True,
                                related_name='event')
    support_contact = models.ForeignKey(settings.AUTH_USER_MODEL,
                                       on_delete=models.SET_NULL,
                                       null=True, blank=True,                                   
                                       related_name='event')
    attendees = models.PositiveIntegerField()
    event_date = models.DateTimeField(null=True, blank=True)
    
    notes = models.TextField(max_length=250, null=True, blank=True)

    event_statut = models.BooleanField(default=False,
                                      verbose_name='Terminé')    

    def __str__(self):
        return f"Event n°{self.id}"

    class Meta:
        verbose_name = "Event"        
        verbose_name_plural = "Events"
