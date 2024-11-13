
from django.urls import path
from Admin import views
app_name="Admin"

urlpatterns = [
    
    path('district/',views.district,name="district"),
    path('deldistrict/<int:id>',views.deldistrict,name="deldistrict"),
    path('editdistrict/<int:id>',views.editdistrict,name="editdistrict"),
    
    path('place/',views.place,name="place"),
    path('delplace/<int:id>',views.delplace,name="delplace"),
    path('editplace/<int:id>',views.editplace,name="editplace"),

]
