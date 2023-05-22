"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from rest_framework import permissions
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi



schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
    public=True,
    permission_classes=[permissions.AllowAny],
    # добавляем фильтры в Swagger
    # manual_parameters=[
    #     openapi.Parameter('category', openapi.IN_QUERY, description="Category of the recipe", type=openapi.TYPE_STRING),
    # ],
)

urlpatterns = [
    # re_path(r'^swagger(?P\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/', include('rest_food.urls')),
    path('admin/', admin.site.urls),
]
# urlpatterns = [
#     # url(r'^$', ),
#     # path('openapi', get_schema_view(
#     #     title="Your Project",
#     #     description="API for all things …"
#     # ), name='api-schema'),
#
#
#     path('swagger-ui/', schema_view),
#
# ]
