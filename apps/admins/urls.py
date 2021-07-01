"""book_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from admins import views

urlpatterns = [
    path('getUsers/', views.GetUsersView.as_view(), name='getUser'),
    path('deleteUser/<int:pk>/', views.DeleteUserView.as_view(), name='deleteUser'),

    path('category/', views.GetCategoryView.as_view(), name='category'),
    path('addBook/', views.AddBookView.as_view(), name='addBook'),
    path('books/', views.GetBooksView.as_view(), name='books'),
]
