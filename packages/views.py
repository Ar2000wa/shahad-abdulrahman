from django.shortcuts import render

# Create your views here.
def Madinah(request):
    return render(request, 'packages/Madinah.html')
def Jeddah(request):
    return render(request, 'packages/Jeddah.html')
def Riyadh(request):
    return render(request, 'packages/Riyadh.html')