"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),


    path('customer-create/', views.CustomerCreateView.as_view(), name='customer-create'),
    path('freelancer-create/', views.FreelancerCreateView.as_view(), name='freelancer-create'),

    path('customer-profile/', views.CustomerProfileView.as_view(), name='customer-profile'),
    path('freelancer-profile/', views.FreelancerProfileView.as_view(), name='freelancer-profile'),

    # path('customer-detail/<int:id>/', views.CustomerDetailView.as_view(), name='customer-detail'),
    # path('freelancer-detail/<int:id>/', views.FreelancerDetailView.as_view(), name='freelancer-detail'),
    
]
