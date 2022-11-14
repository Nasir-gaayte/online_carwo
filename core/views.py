from django.shortcuts import render
from core.models import CategoryModel, PremotionModel
# Create your views here.


def home(request):
    Proms = PremotionModel.objects.all()
    categores = CategoryModel.objects.all()
    return render(request,'core/home.html',{
        'categores':categores,
        'proms':Proms,
        })