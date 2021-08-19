from django.shortcuts import render,redirect
from .models import Tasks
from .forms import TasksForm

# Create your views here.
def homepage(request):
    form=TasksForm()
    if (request.method == 'POST'):
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/home')
    task=Tasks.objects.all()

    context={
            'forms':form,
            'Task':task
    }
    return render(request,'application/home.html',context)



def updatepage(request, pk):
    task=Tasks.objects.get(id=pk)
    form= TasksForm(instance=task)
    if (request.method == 'POST'):
        form= TasksForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/home')

    context={
        'form':form
    }
    return render(request,'application/update.html',context)


def deletepage(request, pk):
    item=Tasks.objects.get(id=pk)
    if (request.method == 'POST'):
        item.delete()
        return redirect('/home')

    context={
        'item':item,
    }
    return render(request,'application/delete.html',context)