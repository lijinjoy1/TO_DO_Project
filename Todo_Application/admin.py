from django.contrib import admin
from .models import Tasks

# Register your models here.
class AdminTasks(admin.ModelAdmin):
    list_display=['title','complete','created']

admin.site.register(Tasks,AdminTasks)