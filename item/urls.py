from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [ 
    path('', views.IndexView.as_view(), name='index'),
    path('about/', views.AboutView.as_view(), name='about'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('process/', views.ProcessView.as_view(), name='process'),
    path('projects/', views.ProjectView.as_view(), name='projects'),
    path('solutions/', views.SolutionView.as_view(), name='solutions'),
]