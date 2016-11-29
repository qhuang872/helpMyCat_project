from django.shortcuts import render
# Create your views here.
from .models import LostFoundAdoptablePets as Pet 
def index(request):
    allpet = Pet.objects.all()
    context = {"allCat":allpet}
    for pet in allpet:
        print pet.obfuscated_latitude
    return render(request,"map/index.html",context)
