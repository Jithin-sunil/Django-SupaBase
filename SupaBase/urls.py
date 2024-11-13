
from django.urls import path,include


urlpatterns = [
    path('Admin/', include('Admin.urls')),
    path('Guest/', include('Guest.urls')),
    path('User/', include('User.urls')),
]
