from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .models import Recruit,Member
from django.views import generic
from .forms import RecruitForm,MemberForm


class IndexView(generic.ListView):
    template_name = "recruit/index.html"
    context_object_name = "recruit_list"
    
    def get_queryset(self):
        """Return the recruit list in alphabetical order!"""
        return Recruit.objects.all().order_by("name")


class DetailView(generic.DetailView):
    model = Recruit
    template_name = "recruit/detail.html"



def add_recruit(request):
    if request.method == 'POST':
        form = RecruitForm(request.POST)
        mem_form=MemberForm(request.POST)
        if form.is_valid() and mem_form.is_valid() :
            rec = form.save()
            mem=mem_form.save(commit=False)
            mem.recruit=rec
            mem.save()
            recruit_list=Recruit.objects.all().order_by('name')
            return HttpResponseRedirect(reverse('recruit:index'))
    else:
        form = RecruitForm()
        mem_form=MemberForm()
        
    return render(request, "recruit/add_recruit.html", {'form': form,'mem_form': mem_form,})

def exist_recruit(request):
    if request.method=='POST':
        mem_form=MemberForm(request.POST)
        if mem_form.is_valid():
            mem=mem_form.save()
            return HttpResponseRedirect(reverse('recruit:index'))
    else:
        mem_form=MemberForm()

    return render(request, "recruit/exist_recruit.html", {'mem_form': mem_form,})


class RecordView(generic.ListView):
    template_name = "recruit/record.html"
    context_object_name = "recruit_list"

    def get_queryset(self):
        """Return the recruit list in alphabetical order!"""
        return Recruit.objects.all().order_by("name")
