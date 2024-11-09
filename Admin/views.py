from django.shortcuts import render,redirect
from django.conf import settings
from supabase import create_client


supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
# Create your views here.

def district(request):
    dis = supabase.table("tbl_district").select().execute()
    district_data = dis.data
    if request.method == 'POST':
        response = supabase.table("tbl_district").insert({"district_name": request.POST.get('txt_dis'),}).execute()
        return redirect("Admin:district")
    else:
        return render(request, 'Admin/District.html',{'district': district_data}) 