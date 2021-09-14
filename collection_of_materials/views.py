from django.shortcuts import render, HttpResponse
from .form import CollectionOfMaterialsForms, Categorie
from .models import CollectionOfMaterials
from .checking_the_types import Forms

def home(request):
    return render(request, "index.html")
def see_urls(request):
    form = Categorie()
    if request.method == "POST":
        dane = request.POST
        category = dane['category']
        print(category)
        model = CollectionOfMaterials.objects
        resultat = model.filter(category=category)
        print(resultat)
        return render(request, "see_urls.html", {'form': form, "category": resultat})
    return render(request, "see_urls.html", {'form': form})
def add_url(request):
    form = CollectionOfMaterialsForms()
    print("POST")
    if request.method == "POST":
        dane = request.POST
        print(dane["title"])
        modelForm = Forms(title=dane["title"], category=dane['category'],
                          url=dane["url"], attention=dane['attention'])
        new_url = form.save(commit=False)
        new_url.attention = modelForm.attention
        new_url.title = modelForm.title
        new_url.category = modelForm.category
        new_url.url = modelForm.url
        print(new_url.title)
        new_url.save()
    return render(request, "add.html", {"form":form})
