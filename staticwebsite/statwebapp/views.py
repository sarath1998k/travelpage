from django.shortcuts import render
from . models import place
from . models import people
# Create your views here.
def demo(request):
    obj = place.objects.all()
    team = people.objects.all()
    return render(request,'index.html',{'result':obj, 'team':team})