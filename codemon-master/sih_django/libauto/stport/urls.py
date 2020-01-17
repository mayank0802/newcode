from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path("", views.rlogin, name = "login_rr"),
#	path("",views.detail, name = "book detail"),
	path("register/", views.register, name = "student_register"),
	path("search/", views.search, name = "book_search"),
    path("feed/", views.feedback, name = "feedback"),
    path('detail/',views.detaiil, name="detail")
]
