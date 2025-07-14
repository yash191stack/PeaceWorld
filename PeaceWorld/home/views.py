from django.shortcuts import render, redirect
from .models import PeaceWorld
from django.contrib import messages

# ====================================================== Home ==============================================================

def home(request):
    return render(request, "home/home.html")

# ====================================================== Dashboard ==============================================================

def dashboard(request):
    return render(request, "home/dashboard.html")

# ====================================================== About ==============================================================

def about(request):
    return render(request, "home/about.html")

# ====================================================== Add Message ==============================================================

def message(request):
    if(request.method == "POST"):
        user_name = request.POST.get("name")
        user_email = request.POST.get("email")
        user_phone = request.POST.get("phone_num")
        user_message = request.POST.get("message")

        # =============================================Creating an object==================================================================
        new_message = PeaceWorld(
            name = user_name,
            email = user_email,
            phone_num = user_phone,
            message = user_message
        )
        new_message.save()
        print("new message added successfully ✅")

        # ========================== Thank You Page with Secret Token ========================================
        return render(request, "home/thankyou.html", {'token': new_message.secret_token})

    return render(request, "home/message.html")

# ====================================================== Show All Messages ==============================================================

def show_message(request):
    show_message = PeaceWorld.objects.all().order_by("-id")

    parameters = {
        "show_message":show_message  
    }

    return render(request,"home/show_message.html",parameters)

# ====================================================== Update Message with Token Check ==============================================================

def update(request, id):
    message = PeaceWorld.objects.get(id=id)

    if request.method == "POST":
        entered_token = request.POST.get("token")

        if entered_token != str(message.secret_token):
            return render(request, "home/unauthorized.html")

        message.name = request.POST.get("name")
        message.email = request.POST.get("email")
        message.phone_num = request.POST.get("phone_num")
        message.message = request.POST.get("message")
        message.is_updated = True

        message.save()
        messages.success(request, "Message updated successfully!")
        return redirect("show_message")

    return render(request, "home/update_message.html", {"message": message})

# ====================================================== Delete Message with Token Check ==============================================================

def delete_message(request, id):
    message = PeaceWorld.objects.get(id=id)

    if request.method == "POST":
        entered_token = request.POST.get("token")

        if entered_token != str(message.secret_token):
            return render(request, "home/unauthorized.html")

        message.delete()
        return redirect("show_message")

    return render(request, "home/delete_message.html", {"message": message})
