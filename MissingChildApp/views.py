from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Home Page
def Index(request):
    return render(request, "index.html")

# Public Upload Page
def Upload(request):
    return render(request, "upload.html")

# Handle Upload Action
def UploadAction(request):
    if request.method == "POST":
        # your upload saving logic
        messages.success(request, "Upload successful")
        return redirect("upload")
    return redirect("upload")

# ✅ Official Login (Custom, not Django Admin)
def OfficialLogin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("officialscreen")   # redirect to dashboard
        else:
            messages.error(request, "Invalid Username or Password")
            return redirect("official_login")

    return render(request, "OfficialLogin.html")

# Dashboard after login
@login_required
def OfficialScreen(request):
    return render(request, "OfficialScreen.html")

# View Uploaded Children
@login_required
def ViewChildren(request):
    # Fetch records from DB (replace with your model)
    children = []  
    return render(request, "ViewUpload.html", {"children": children})