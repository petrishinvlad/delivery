from django.urls import path
from book import views

app_name = 'book'

urlpatterns = [
    path('/', views.index, name='index'),
    path('/<int:age>/', views.show_age, name='show_age'),
    path('/name/<str:name>/', views.show_name, name='show-name')
]