from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render

from .models import *


# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def cv(request, phone):
    base_infor = BaseInformation.objects.get(phone=phone)
    lst_skills = Skill.objects.filter(user=base_infor)
    lst_education = Education.objects.filter(user=base_infor).order_by(F('end_date').desc())
    lst_certifications = Certification.objects.filter(user=base_infor).order_by(F('time').desc())
    lst_projects = Project.objects.filter(user=base_infor).order_by(F('time_end').desc())
    lst_experiences = Experience.objects.filter(user=base_infor).order_by(F('time_end').desc())
    data = {
        'base_infor': base_infor,
        'lst_skills': lst_skills,
        'lst_education': lst_education,
        'lst_certifications': lst_certifications,
        'lst_projects': lst_projects,
        'lst_experiences': lst_experiences,
    }
    return render(request, 'cv_app/index.html', context=data)
