from django.shortcuts import render, redirect
from django.conf import settings
from supabase import create_client
import uuid

# Initialize Supabase client
supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)



def user(request):
    dis = supabase.table("tbl_district").select().execute()
    district_data = dis.data
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        photo = request.FILES.get('photo')
        auth_response = supabase.auth.sign_up({
            "email": email,
            "password": password,
        })
        if auth_response.user:
            user_data = auth_response.user  
            user_id = user_data.id
            place_id = request.POST.get('sel_place')

            file_name = f"UserDocs/{user_id}_{uuid.uuid4()}_{photo.name}"
            photo_content = photo.read()
            storage_response = supabase.storage.from_("django").upload(file_name, photo_content)
            photo_url = supabase.storage.from_("django").get_public_url(file_name)
            

            # Insert user data into the database, including the photo URL
            insert_response = supabase.table("tbl_user").insert({
                "user_name": request.POST.get('name'),
                "user_email": email,
                "user_contact": request.POST.get('contact'),
                "user_address": request.POST.get('address'),
                "user_password": password, 
                "place_id": place_id,
                "user_id": user_data.id,
                "user_photo": photo_url  # Save the photo URL in the `user_photo` field
            }).execute()
        
        return redirect("Guest:user")  
    else:
        return render(request, "Guest/User.html", {'district': district_data})


def ajaxplace(request):
    district_id = request.GET.get('did')
    place = supabase.table("tbl_place").select("*, tbl_district(*)").eq('district_id', district_id).execute()
    place_data = place.data
    return render(request, "Guest/Ajaxplace.html", {'place': place_data})

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        auth_response = supabase.auth.sign_in_with_password({
            "email": email,
            "password": password,
        })
       
        if auth_response.user:
            
            auth_user_id = auth_response.user.id
            # print(auth_user_id)

            
            user_data = supabase.table("tbl_user").select("user_id").eq("user_id", auth_user_id).execute()

          
            if user_data.data:
                request.session['uid']=auth_user_id
                
                return redirect("User:homepage")
            else:
                return render(request, "Guest/Login.html")
        
        else:
            return render(request, "Guest/Login.html")
    else:
        return render(request, "Guest/Login.html")