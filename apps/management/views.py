from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from apps.management.forms import EmployeeForm
from apps.management.models import Employee


def emplo(request):
    return HttpResponse('Hello world')

class CreateCustomer(CreateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'form.html'
    success_url = reverse_lazy('create-employ-list')

class CustomerList(ListView):
    model = Employee
    template_name = 'list.html'
    context_object_name = 'employees'


class CustomerUpdate(UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name = 'update.html'
    success_url = reverse_lazy('create-employ-list')


class CustomerDelete(DeleteView):
    model = Employee
    template_name = 'conform_delete.html'
    success_url = reverse_lazy('create-employ-list')



