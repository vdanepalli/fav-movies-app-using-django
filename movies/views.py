from django.shortcuts import render, HttpResponse


# Create your views here.
my_fav_movies = [
    {
        "title": "Top Gun"
    },
    {
        "title": "My Cousin Vinny"
    },
    {
        "title": "Twelve Angry Men"
    }
]

def index(request):
    context = {
        "movies": my_fav_movies
    }
    
    return render(request, "movies/index.html", context)

def about(request):
    return render(request, "movies/about.html")
    