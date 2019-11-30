from django import forms
from .models import Meal, Food

class MealForm(forms.ModelForm):
	class Meta:
		model = Meal
		fields = "__all__"

class FoodForm(forms.ModelForm):
	class Meta:
		model = Food
		fields = "__all__"