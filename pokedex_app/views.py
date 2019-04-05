from django.shortcuts import render
from django.views import View
from .models import Pokemon

# Create your views here.


class Home(View):
    def get(self, request):

        pokemon = Pokemon.objects.all().order_by("nationalId")

        context = {
            "pokemon": pokemon
        }

        return render(request, 'home.html', context)

class Details(View):
    def get(self, request ,id):

        pokemon = Pokemon.objects.get(id=id)

        context = {
            "pokemon": pokemon
        }

        return render(request, 'details.html', context)
