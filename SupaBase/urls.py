
from django.urls import path,include

urlpatterns = [
    path('admin/', include('Admin.urls')),
]
