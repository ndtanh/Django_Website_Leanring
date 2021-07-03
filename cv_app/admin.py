from django.contrib import admin

from .models import *


# Register your models here.
class BaseInformationAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email']
admin.site.register(BaseInformation, BaseInformationAdmin)


class EducationAdmin(admin.ModelAdmin):
    list_display = ['school', 'major', 'GPD']
admin.site.register(Education, EducationAdmin)


class SkillAdmin(admin.ModelAdmin):
    list_display = ['skill_name']
admin.site.register(Skill, SkillAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
admin.site.register(Project, ProjectAdmin)


class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'time']
admin.site.register(Certification, CertificationAdmin)


class ActivityAdmin(admin.ModelAdmin):
    list_display = ['name', 'position']
admin.site.register(Activity, ActivityAdmin)


class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'position']
admin.site.register(Experience, ExperienceAdmin)