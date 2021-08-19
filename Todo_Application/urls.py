from django.urls import path
from Todo_Application import views

urlpatterns = [
    path('home/',views.homepage,name='home'),
    path('update/<str:pk>',views.updatepage,name='update_task'),
    
]
