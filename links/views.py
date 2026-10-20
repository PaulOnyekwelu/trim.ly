from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpRequest
from .models import Link
from .forms import LinkForm

# Create your views here.
def index(request: HttpRequest):

    links = Link.objects.all()
    context = {
        "links": links
    }

    return render(request, "links/index.html", context)


def root_link(request: HttpRequest, slug: str):
    link = get_object_or_404(Link, slug=slug)
    link.click()

    return redirect(link.url)

def create_link(request: HttpRequest):
    # return render(request, "links/create_link.html", {})
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("home"))

    elif request.method == "GET":
        form = LinkForm()
        context = {
            "form": form
        }
        return render(request, "links/create_link.html", context)
    
    return redirect(reverse("home"))