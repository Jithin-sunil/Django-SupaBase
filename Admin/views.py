from django.shortcuts import render,redirect
from django.conf import settings
from supabase import create_client
from Admin.models import *


supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
# Create your views here.

# def district(request):
#     dis = supabase.table("tbl_district").select().execute()
#     district_data = dis.data
#     if request.method == 'POST':
#         response = supabase.table("tbl_district").insert({"district_name": request.POST.get('txt_dis'),}).execute()
#         return redirect("Admin:district")
#     else:
#         return render(request, 'Admin/District.html',{'district': district_data}) 


def district(request):
    district_data = District.objects.all()
    if request.method == 'POST':
        district_name = request.POST.get('txt_dis')
        if district_name:
            District.objects.create(district_name=district_name)
        return redirect("Admin:district")
    else:
        return render(request, 'Admin/District.html', {'district': district_data})


def deldistrict(request,id): 
    delete = supabase.table('tbl_district').delete().eq('id', id).execute()
    return redirect("Admin:district")


def editdistrict(request,id):
    dis = supabase.table("tbl_district").select().eq('id', id).single().execute()
    district_data = dis.data
    if request.method == 'POST':
        response = supabase.table("tbl_district").update({"district_name": request.POST.get('txt_dis')}).eq('id',id).execute()
        return redirect("Admin:district")
    else:
        return render(request, 'Admin/District.html', {'edit': district_data})


def place(request):
    dis= supabase.table("tbl_district").select().execute()
    district_data = dis.data
    place= supabase.table("tbl_place").select("*,tbl_district(*)").execute()
    place_data = place.data
    # print(place_data)
    if request.method == 'POST':
        response = supabase.table("tbl_place").insert({"place_name": request.POST.get('txt_place'), "district_id": request.POST.get('sel_district')}).execute()
        return redirect("Admin:place")
    else:
        return render(request, 'Admin/Place.html',{'district':district_data, 'place':place_data})   

def delplace(request,id):
    delete = supabase.table('tbl_place').delete().eq('id', id).execute()
    return redirect("Admin:place")

def editplace(request,id):
    dis= supabase.table("tbl_district").select().execute()
    district_data = dis.data
    place= supabase.table("tbl_place").select("*,tbl_district(*)").eq('id', id).single().execute()
    place_data = place.data
    if request.method == 'POST':
        response = supabase.table("tbl_place").update({"place_name": request.POST.get('txt_place'), "district_id": request.POST.get('sel_district')}).eq('id',id).execute()
        return redirect("Admin:place")
    else:
        return render(request, 'Admin/Place.html', {'edit': place_data, 'district': district_data})