from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
#  from rest_framework.authtoken import views

from api.urls import urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urlpatterns), name='api'),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
    # path('api/', include('api.urls')),
    #  path('api-token-auth/', views.obtain_auth_token),
]
