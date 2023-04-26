from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render
from rentcar.models import Car


class CarListView(TemplateView):
    template_name = 'home.html'


#
class CarListView(ListView):
    queryset = Car.objects.all()
    template_name = 'home.html'
    context_object_name = 'cars'


# class salom(DetailView):
#     queryset = Car.objects.all()


class CarDetailView(DetailView):
    queryset = Car.objects.all()
    template_name = 'cars/car_detail.html'
    context_object_name = 'car'


def cardetail(req, pk):
    car = Car.objects.get(id=pk)
    context = {
        'car': car
    }
    return render(req, 'cars/car_detail.html', context)


class CarCategories(ListView):
    queryset = Car.objects.all()
    template_name = 'cars/car_categories.html'
    context_object_name = 'categories'


class BuyNow(DetailView):
    queryset = Car.objects.all()
    template_name = 'cars/buy_now.html'
    context_object_name = 'buy'


class Discount(ListView):
    queryset = Car.objects.order_by('-id')
    template_name = 'cars/discount.html'
    context_object_name = 'discount'
