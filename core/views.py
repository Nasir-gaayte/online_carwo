from django.shortcuts import render, redirect
from core.models import CategoryModel, PremotionModel, ShopModel
# Create your views here.


def home(request):
    Proms = PremotionModel.objects.all()
    categores = CategoryModel.objects.all()
    shops  = ShopModel.objects.all()
    return render(request,'core/home.html',{
        'categores':categores,
        'proms':Proms,
        'shops':shops,
        })
    
    
def add_shop(request):
    categores = CategoryModel.objects.all() 
    shops  = ShopModel.objects.all()
    # for categores in CategoryModel.objects.all(): 
    if request.method == "POST":
        data = request.POST
        username = request.user
        print(username)
        title_image = request.FILES.get('title_image')
        images = request.FILES.getlist ('images')
        category = CategoryModel.objects.get(id = data['category']) 
         
        for shop in shops:
            shop = ShopModel.objects.get_or_create(
                username = username,
                # category = data['category'],
                category = category,
                description = data['description'],
                title_image = title_image,
                images = images,
            )
        return redirect ('home')
    return render(request,'core/add_shop.html',{'categores':categores,})