from django.shortcuts import render
from django.http import HttpResponse
from .models import Clothes

# Create your views here.
def home(request):
    clothes = Clothes.objects.all()
    return render(request,'home.html', {
        'clothes': clothes,
        })

def clothes_detail(request, clothes_id):
    try:
        clothes = Clothes.objects.get( id = clothes_id)
    except Clothes.DoesNotExist:
        raise Http404('Cloth not found')
    return render(request, 'clothes_detail.html', {
        'clothes' : clothes,
        })