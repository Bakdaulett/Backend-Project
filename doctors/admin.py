from django.contrib import admin
from .models import Footballer, Statistics, Clubs


class MemberAdmin(admin.ModelAdmin):
    list_display = ("name", "price", "age")


class MemberAdmin2(admin.ModelAdmin):
    list_display = ("f_name", "goal", "assist", "game", "club")


class MemberAdmin3(admin.ModelAdmin):
    list_display = ("c_name", "manager")


admin.site.register(Footballer, MemberAdmin)
admin.site.register(Statistics, MemberAdmin2)
admin.site.register(Clubs, MemberAdmin3)
