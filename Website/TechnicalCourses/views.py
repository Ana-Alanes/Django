from django.shortcuts import render

from django.http import HttpResponse, Http404
from .models import Allcourses
from django.template import loader


def Courses(request):
    ac=Allcourses.objects.all()
    template=loader.get_template('/TechnicalCourses/Courses.html')
    context={
        'ac': ac,
    }
    return HttpResponse(template.render(context, request))


def detail(request, couse_id):
    try:
        course=Allcourses.objects.get(pk=couse_id)
    except Allcourses.DoesNotExist:
        raise Http404("Course Not Available")
    return render(request, 'TechnicalCourses/detail.html', {'course':course})

