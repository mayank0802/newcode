from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
	path("bk_info/",views.bkinfo, name = "bk_info"),
	path("issue/", views.bk_issue, name = "bk_issue"),
	path("return/", views.retrn, name= 'bk_return'),
    path("flogin/", views.libb, name = 'lib_aDin'),
    path("admin_home/", views.admin_home, name = "admin_home"),
    path('notice/', views.noticce, name = "notice"),
    path('', views.home, name = 'home')
]
