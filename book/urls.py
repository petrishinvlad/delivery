from django.urls import path
from book import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:age>/', views.show_age, name='show_age')
]