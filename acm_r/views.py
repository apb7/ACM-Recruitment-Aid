from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

def home(request):
    return HttpResponseRedirect(reverse("recruit:index"))
