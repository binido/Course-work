from django.contrib import admin

from .models import Master, Skills, Workarea

# @admin.register(Master)
# class MasterAdmin(admin.ModelAdmin):
#     list_display = ('name', 'experience')


admin.site.register(Master)
admin.site.register(Skills)
admin.site.register(Workarea)
