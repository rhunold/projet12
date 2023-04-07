from django.contrib import admin
from django.urls import path, include

from rest_framework import routers


from crm.views import (EmployeeViewset, 
                       ClientViewset, ContractViewset, EventViewset,
                       test_error) 

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


router = routers.SimpleRouter()
router.register('employees', EmployeeViewset, basename='employees')
router.register('clients', ClientViewset, basename='clients')
router.register('contracts', ContractViewset, basename='contracts')
router.register('events', EventViewset, basename='events')




urlpatterns = [
    path('admin/', admin.site.urls),

    # Web browsable API (for login and logout)
    path("api/", include("rest_framework.urls", namespace='rest_framework')),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # Endpoint API    
    path('', include(router.urls)),
    
    path('test_error/',test_error, name="test_error")

]


admin.site.site_header = "Epic Events Admin"
admin.site.index_title = "Epic Events"

