from django.contrib import admin
from .models import *


# Register your models here.

class SubAdmin(admin.ModelAdmin):
    list_display = ["name", "email"]
    list_filter = ["name", "email"]
    search_fields = ['name', "email"]

    class Meta:
        model = Subscribers


admin.site.register(Subscribers, SubAdmin)
admin.site.register(Band)
admin.site.register(ConcertAgency)
admin.site.register(BandUsername)
admin.site.register(CA_Band)
