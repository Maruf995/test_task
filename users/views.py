from .models import *
from .forms import *
from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.views.generic.edit import FormMixin

def index(request):
    return render(request, 'base.html')


class CustomerCreateView(CreateView):
    template_name = 'customer_create.html'
    form_class = CustomerForm
    queryset = Customer.objects.all()

    def form_valid(self, form):
        return super().form_valid(form=form)
    

class FreelancerCreateView(CreateView):
    template_name = 'customer_create.html'
    form_class = FreelancerForm
    queryset = Freelancer.objects.all()

    def form_valid(self, form):
        return super().form_valid(form=form)
    

class FreelancerProfileView(ListView):
    template_name = 'freelancer_profile.html'
    model = Freelancer

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = Task.objects.all()  # Используем 'task_list' вместо 'task'
        return context

class CustomerProfileView(CreateView, ListView):
    template_name = 'customer_profile.html'
    queryset = Customer.objects.all()
    form_class = TaskForm


    def get_queryset(self):
        return Customer.objects.all()
    
    def form_valid(self, form):
        return super().form_valid(form=form)


# class TaskListView(ListView):
#     template_name = 'freelancer_profile.html'
#     queryset = Freelancer.objects.all()

#     def get_queryset(self):
#         return Freelancer.objects.all()