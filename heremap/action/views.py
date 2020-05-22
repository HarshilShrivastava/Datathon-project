from django.shortcuts import render
from .models import data
from project.models import Pune_POI
from .forms import get_data

from django.views.generic import TemplateView
from django.core.serializers import serialize
from django.http import HttpResponse

# Create your views here.
class HomePageView(TemplateView):
	template_name = 'add.html'

def point_datasets(request):
	points = serialize('geojson', Pune_POI.objects.all()[0:500])
	return HttpResponse(points,content_type='json')

# Create your views here.
def putdata(request):
    forms=get_data(request.POST)
    qs = Pune_POI.objects.all()
    if forms.is_valid():
        for each in qs:
            if each.Lat == forms.cleaned_data["User_lat"] and each.Lon == forms.cleaned_data["User_lon"]:
                instance = forms.save(commit=False)
                instance.ST_NAME = each.ST_NAME
                instance.POI_NAME = each.POI_NAME
                instance.save()
                break
        forms.save()
    else:
        forms=get_data()
    return render(request,"form.html",{"form":forms})   

def project_iframe(request):
    return render(request, 'frame.html')

     
def CommentSee(request):
    qs=data.objects.all()
    return render(request,'comment.html',{"qs":qs})

