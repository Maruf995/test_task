from django import forms
from .models import *


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = [
            'username',
            'number',
            'email'
        ]

class FreelancerForm(forms.ModelForm):
    class Meta:
        model = Freelancer
        fields = [
            'username',
            'number',
            'email',
            'experience'
        ]


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'price'
        ]