from django.contrib import admin
from .models import Master, Skills, Workarea, PortfolioImage, MasterTasks, Feedbacks, Service


class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1  # Количество пустых полей для загрузки изображений


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('name', 'experience')
    inlines = [PortfolioImageInline]


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    list_display = ('name', 'cat_name', 'slug')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'skill')
    search_fields = ('name', 'skill__name')
    list_filter = ('skill',)


@admin.register(Workarea)
class WorkareaAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')


@admin.register(PortfolioImage)
class PortfolioImageAdmin(admin.ModelAdmin):
    list_display = ('master', 'image')


@admin.register(MasterTasks)
class MasterTasksAdmin(admin.ModelAdmin):
    list_display = ('master_type', 'client_name', 'client_tel', 'client_adders', 'status')
    list_editable = ('status',)
    list_filter = ('status',)
    search_fields = ('client_name', 'client_tel', 'client_adders')


@admin.register(Feedbacks)
class FeedbacksAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at')
