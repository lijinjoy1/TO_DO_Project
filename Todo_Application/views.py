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
    return render(request,'application/update.html')
