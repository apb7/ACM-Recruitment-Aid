from django import forms
from .models import Recruit,Member
#from django.forms import inlineformset_factory

#MemberFormSet=inlineformset_factory(Recruit,Member,fields=('remarks','grilled_by','task',))

class RecruitForm(forms.ModelForm):
    class Meta:
        model=Recruit
        fields='__all__'

class MemberForm(forms.ModelForm):
    class Meta:
        model=Member
        fields='__all__'
