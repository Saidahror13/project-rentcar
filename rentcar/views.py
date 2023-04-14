from django.views.generic import ListView, DetailView
from django.shortcuts import render
from rentcar.models import Car


class CarListView(ListView):
    queryset = Car.objects.all()
    template_name = 'home.html'
    context_object_name = 'cars'


class salom(DetailView):
    queryset = Car.objects.all()


class CarDetailView(DetailView):
    queryset = Car.objects.all().first()
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'


def cardetail(req, pk):

    context = {
        'car': Car.objects.get(id=pk)
    }
    return render(req, 'cars/car_detail.html', context)