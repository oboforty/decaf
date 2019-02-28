from django.urls import path
from . import views
from django.conf.urls import url
from mysite.search import views

"""search"""
urlpatterns = [
    url(r'^search/$', views.search, name='search'),




app_name = 'scan'
urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('scans/', views.scan_list, name='scans'),
    path('patients/', views.patient_list, name='patients'),

    path('upload_form/', views.change, name='upload_form'),
    path('test/', views.test, name='test'),

    path('add/', views.add, name='add'),
    path('edit/<int:pid>/', views.edit, name='edit'),
    path('delete/<int:pid>/', views.delete, name='delete'),
    path('view/<int:pid>/', views.view, name='view')
]
