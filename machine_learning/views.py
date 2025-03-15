from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def machine_learnig(request):
    return render(request,'machineLearning.html')