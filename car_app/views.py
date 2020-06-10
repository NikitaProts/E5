# from django.shortcuts import render
# from car_app.models import Car
# from car_app.forms import CarForm
#
#
# def car_list(request):
#     form = CarForm()
#     cars = Car.objects.all()
#     return render(request, 'list.html', {'cars': cars, 'form': form})

from django.db.models import Q
from django.views.generic import TemplateView
from car_app.models import Car


class CarView(TemplateView):
    template_name = 'list.html'

    def get_context_data(self, **kwargs):
        params = self.request.GET
        query = Q()
        for key, value in params.items():
            if value and key in vars(Car):
                query &= Q(**{key: value})
        return {'cars': Car.objects.filter(query)}
