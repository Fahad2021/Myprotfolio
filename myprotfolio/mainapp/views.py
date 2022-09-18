from django.shortcuts import render
from mainapp.models import MainAPP


def project_index(request):
    projects = MainAPP.objects.all()
    context = {"projects": projects}
    return render(request, "project_index.html", context)


def project_detail(request, pk):
    project = MainAPP.objects.get(pk=pk)
    context = {"project": project}
    return render(request, "project_detail.html", context)