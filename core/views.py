from django.shortcuts import render
from core.models import CategoryModel
# Create your views here.


def home(request):
    
    categores = CategoryModel.objects.all()
    return render(request,'core/home.html',{'categores':categores})