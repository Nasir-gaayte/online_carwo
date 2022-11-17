from django import forms
from core.models import ShopModel


class ShopForm(forms.ModelForm):
    class Meta:
        model = ShopModel
        fields = ("category","title", "title_image", "images", "description")