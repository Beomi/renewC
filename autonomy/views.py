from django.shortcuts import render
from .models import Petition

#def index(request):
#    return render(request, 'index.html')

def index(request):
    p = Petition.objects.first()
    return render(request, 'index.html', {'p': p})