from django import views
from django.urls import path
from . import views 

app_name = 'test_app'

urlpatterns = [
    path('', views.Index.as_view(), name = 'index'),
    path('add', views.Add.as_view(), name = 'add'),
    path('person', views.People.as_view(), name = 'person'),
    path('all_person', views.All_Person.as_view(), name = 'all_person')
]