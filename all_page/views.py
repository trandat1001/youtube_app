from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, "all_page/index.html")

def about_view(request):
    return render(request, "all_page/about.html")

def privacy_view(request):
    return render(request, "all_page/privacy.html")
