from django.shortcuts import render
from django.views import View
from .models import Pokemon, Evolution
from django.db.models import Q
from django.shortcuts import redirect

# Create your views here.


class Root(View):
    def get(self, request):

        return redirect("home")


class Home(View):
    def get(self, request):

        pokemon = Pokemon.objects.all().order_by("nationalId")

        context = {"pokemon": pokemon}

        return render(request, 'home.html', context)


class Details(View):
    def get(self, request, id):

        pokemon = Pokemon.objects.get(id=id)

        context = {
            "pokemon": pokemon,
            "evolutions": pokemon.evolves_from_set.all()
        }
        return render(request, 'details.html', context)


class Search(View):
    def get(self, request):

        pokemon = Pokemon.objects.all().order_by("nationalId")

        query = request.GET.get("name")

        if query:
            query_list = pokemon.filter(Q(name__icontains=query))
            context = {"pokemon": query_list}
            return render(request, 'search.html', context)

        else:
            return render(request, 'search.html')


class Filter(View):
    def get(self, request):

        pokemon = Pokemon.objects.all().order_by("nationalId")

        query = request.GET.get("type")

        if query:
            query_list = pokemon.filter(Q(pokemonType__icontains=query))
            context = {"pokemon": query_list}
            return render(request, 'filter.html', context)

        else:
            return render(request, 'filter.html')
