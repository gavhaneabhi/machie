from django.contrib import admin
from django.urls import include, path
from myapp import views



urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index, name='index',),
    path('results', views.results, name='results'),
    path('graph', views.graph, name='graph'),
    ]