from django.contrib import admin
from  core.models import CategoryModel, PremotionModel, ShopModel
# Register your models here.




admin.site.register(CategoryModel)
admin.site.register(PremotionModel)
admin.site.register(ShopModel)