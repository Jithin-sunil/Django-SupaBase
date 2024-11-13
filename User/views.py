from django.shortcuts import render,redirect
from django.conf import settings
from supabase import create_client
# Create your views here.
supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
def homepage(request):
   
    return render(request, 'User/Homepage.html')

def profile(request):
    user_id = request.session.get('uid')  
    user = supabase.table("tbl_user").select().eq("user_id", user_id).execute()
    user_data = user.data[0]
    # print(user_data)
    return render(request, 'User/MyProfile.html', {'user': user_data})
 
       
