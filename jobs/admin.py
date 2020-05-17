from django.contrib import admin

from .models import Company, Specialty, Vacancy

class CompanyAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "location", "description", "employee_count") 
    search_fields = ("name",) 
    list_filter = ("name",) 
    empty_value_display = '-пусто-'	

class VacancyAdmin(admin.ModelAdmin):
    list_display = ("pk", "title", "specialty", "description", "company") 
    search_fields = ("title",) 
    list_filter = ("title",) 
    empty_value_display = '-пусто-'	



admin.site.register(Company, CompanyAdmin)
admin.site.register(Specialty)
admin.site.register(Vacancy, VacancyAdmin)

