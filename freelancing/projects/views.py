from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Project
from .forms import project_form
# Create your views here.

def projects(request):
    projects =Project.objects.all()
    context = {'projects':projects,}
    return render(request,'projects/index.html',context)

def project(request,pk):
    project = Project.objects.get(id=pk)
    context ={'project':project}
    return render(request,'projects/projects.html',context)

def create_project(request):
    form = project_form()

    if request.method =='POST':
        form = project_form(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projects')

    context = {'form':form}
    return render(request,"projects/project_form.html",context)



def update_project(request,pk):
    project = Project.objects.get(id=pk)
    form = project_form(instance=project)

    if request.method == 'POST':
        form = project_form(request.POST,request.FILES, instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form':form}
    return render(request,'projects/project_form.html',context)


def delete_project(request,pk):
    project =Project.objects.get(id=pk)
    if request.method =="POST":
        project.delete()
        return redirect('projects')
    context = {'object':[project]}
    return render(request,'projects/delete_template.html',context)