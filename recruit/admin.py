from django.contrib import admin
from .models import Recruit,Member
# Register your models here.


class MemberInline(admin.TabularInline):
    model = Member
    extra = 3


class RecruitAdmin(admin.ModelAdmin):
    inlines = [MemberInline]
    search_fields = ['name']


admin.site.register(Recruit, RecruitAdmin)
