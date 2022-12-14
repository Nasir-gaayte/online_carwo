from django.shortcuts import render, redirect
from core.models import CategoryModel, PremotionModel, ShopModel
from core.forms import ShopForm
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
        images = request.FILES.get ('images')
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


def detail(request, id):
    shop = ShopModel.objects.get(pk = id)
    
    return render(request,'core/detail.html',{'shop':shop})


def update_shop(request, id):
    shop = ShopModel.objects.get(pk =id)
    if request.method == "POST":
        form = ShopForm(request.POST, instance=shop)
        if form.is_valid():
            form.save()  
            return redirect ('home')
    form = ShopForm(instance=shop)
    return render(request,'core/update_shop.html',{
        'form':form,
        })    