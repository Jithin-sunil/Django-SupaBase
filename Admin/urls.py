
from django.urls import path
from Admin import views
app_name="Admin"

urlpatterns = [
    
    path('district/',views.district,name="district"),
]
