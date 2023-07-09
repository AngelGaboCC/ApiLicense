
from django.contrib import admin
from django.urls import path
from ApiLicense import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('licenses/', views.license_list),
    path('licenses/<int:id>', views.license_detail)
]

urlpatterns = format_suffix_patterns(urlpatterns)
