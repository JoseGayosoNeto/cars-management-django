from django.shortcuts import render, redirect
from django.views import View
from cars.models import Car
from cars.forms import NewCarModelForm

class CarsView(View):
    
    def get(self, request):
        cars = Car.objects.all().order_by('model')
        
        query_params = request.GET.get('search')
        if query_params:
            cars = cars.filter(model__icontains=query_params)
            
        return render(request, 'cars.html', {'cars': cars})

class NewCarView(View):
    
    def get(self, request):
        new_car_form = NewCarModelForm()
        return render(request, 'new_car.html', {'new_car_form': new_car_form})
    
    def post(self, request):
        new_car_form = NewCarModelForm(request.POST, request.FILES)
        if new_car_form.is_valid():
            new_car_form.save()
            return redirect('cars_list')
        return render(request, 'new_car.html', {'new_car_form': new_car_form})