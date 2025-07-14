# from django.shortcuts import render,redirect
# from .models import PeaceWorld
# from django.contrib import messages


# # Create your views here.

# def home(request):
#     return render(request,"home/home.html")

# def dashboard(request):
#     return render(request, "home/dashboard.html")

# def about(request):
#     return render(request, "home/about.html")

# def message(request):
#     if(request.method=="POST"):
#         user_name = request.POST.get("name")
#         user_email = request.POST.get("email")
#         user_phone = request.POST.get("phone_num")
#         user_message = request.POST.get("message")

#     # =============================================Creating an object==================================================================
#         new_message = PeaceWorld(
#         name = user_name,
#         email = user_email,
#         phone_num = user_phone,
#         message = user_message
#     )
#         new_message.save()
#         print("new message added successfully")
#         return redirect("show_message")

#     return render(request, "home/message.html")

# def show_message(request):
#     show_message = PeaceWorld.objects.all().order_by("-id")

#     parameters = {
#         "show_message":show_message  
#         # "html names":python name
#     }

#     return render(request,"home/show_message.html",parameters)

# # ======================================================Delete===============================================================

# def delete_message(request,id):
#     message = PeaceWorld.objects.get(id=id)
#     message.delete()
#     return redirect("show_message")

# def update(request,id):
#     message = PeaceWorld.objects.get(id=id)
#     if request.method=="POST":
#         message.name = request.POST.get("name")
#         message.email = request.POST.get("email")
#         message.phone_num = request.POST.get("phone_num")
#         message.message = request.POST.get("message")
#         message.is_updated = True
#         messages.success(request, "Message updated successfully!") 

#         message.save()
#         return redirect("show_message")


#     return render(request,"home/update_message.html",{"message": message})

# ✅ Updated views.py with token-based ownership
from django.shortcuts import render, redirect
from .models import PeaceWorld
from django.contrib import messages

# Home page

def home(request):
    return render(request, "home/home.html")

# Dashboard

def dashboard(request):
    return render(request, "home/dashboard.html")

# About

def about(request):
    return render(request, "home/about.html")

# Add new message with token generation
def message(request):
    if request.method == "POST":
        user_name = request.POST.get("name")
        user_email = request.POST.get("email")
        user_phone = request.POST.get("phone_num")
        user_message = request.POST.get("message")

        new_message = PeaceWorld(
            name=user_name,
            email=user_email,
            phone_num=user_phone,
            message=user_message
        )
        new_message.save()

        return render(request, "home/thankyou.html", {'token': new_message.secret_token})

    return render(request, "home/message.html")

# Show all messages
def show_message(request):
    show_message = PeaceWorld.objects.all().order_by("-id")
    parameters = {"show_message": show_message}
    return render(request, "home/show_message.html", parameters)

# Delete with token verification
def delete_message(request, id):
    token = request.GET.get('token')
    msg = PeaceWorld.objects.get(id=id)

    if str(msg.secret_token) != token:
        return render(request, 'home/unauthorized.html')

    msg.delete()
    return redirect("show_message")

# Update with token verification
def update(request, id):
    token = request.GET.get('token')
    msg = PeaceWorld.objects.get(id=id)

    if str(msg.secret_token) != token:
        return render(request, 'home/unauthorized.html')

    if request.method == "POST":
        msg.name = request.POST.get("name")
        msg.email = request.POST.get("email")
        msg.phone_num = request.POST.get("phone_num")
        msg.message = request.POST.get("message")
        msg.is_updated = True
        messages.success(request, "Message updated successfully!")
        msg.save()
        return redirect("show_message")

    return render(request, "home/update_message.html", {"message": msg})
