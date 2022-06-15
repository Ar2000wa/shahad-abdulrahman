from django.shortcuts import render
from . models import Beauty
from . models import Fashion
from . models import Weddings
# Create your views here.
def beauty(request):
    post = Beauty.objects.all()
    return render(request, 'gallery/beauty.html',{'post':post})
def fashion(request):
    post = Fashion.objects.all()
    return render(request, 'gallery/fashion.html',{'post':post})
def weddings(request):
    post = Weddings.objects.all()
    return render(request, 'gallery/weddings.html',{'post':post})

