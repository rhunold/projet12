
from django.contrib import admin
from django.urls import path, include
# from authentication.admin import manager_site


from crm.views import ClientViewset, ContractViewset, EventViewset #SignUpView, ContributorsViewset, ProjectViewset, IssueViewset, CommentViewset

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework_nested import routers


client_router = routers.SimpleRouter()
client_router.register('clients', ClientViewset, basename='clients')

contract_router = routers.SimpleRouter()
contract_router.register('contracts', ContractViewset, basename='contracts')

event_router = routers.SimpleRouter()
event_router.register('events', EventViewset, basename='events')

# users_router = routers.NestedSimpleRouter(client_router, 'clients', lookup='clients')
# users_router.register('users', ContractViewset, basename='contracts')

# issues_router = routers.NestedSimpleRouter(project_router, 'projects', lookup='project')
# issues_router.register('issues', IssueViewset, basename='issues')

# comments_router = routers.NestedSimpleRouter(issues_router, 'issues', lookup='issue')
# comments_router.register('comments', CommentViewset, basename='comments')


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('manager_admin/', manager_site.urls),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', include(client_router.urls)),
    path('', include(contract_router.urls)),
    path('', include(event_router.urls)),    
    # path('', include(issues_router.urls)),
    # path('', include(comments_router.urls)),    
]


admin.site.site_header = "Epic Events Admin"
admin.site.index_title = "Epic Events"

