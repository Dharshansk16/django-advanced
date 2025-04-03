from django import forms
from .models import Rating, Restaurant

class RestaurantForm(forms.ModelForm):
    # class Meta:
    #     model =Rating
    #     fields=("restaurant", "user", "rating")
    class Meta:
        model= Restaurant
        fields=("name",)
