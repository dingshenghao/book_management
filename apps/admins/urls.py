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
from rest_framework.routers import DefaultRouter

from admins import views

router = DefaultRouter()
router.register('search', views.BookSearchViewSet, basename='book_search')

urlpatterns = [
    path('getUsers/', views.GetUsersView.as_view(), name='getUser'),
    path('deleteUser/<int:pk>/', views.DeleteUserView.as_view(), name='deleteUser'),

    path('category/', views.GetCategoryView.as_view(), name='category'),
    path('addBook/', views.AddBookView.as_view(), name='addBook'),
    path('books/', views.GetBooksView.as_view(), name='books'),
    path('editBook/<int:pk>/', views.EditBookView.as_view(), name='editBook'),
    path('deleteBook/<int:pk>/', views.DeleteBookView.as_view(), name='deleteBook'),

    path("getBorrow/", views.GetBorrowsBook.as_view(), name='getBorrow'),
    path("getBorrow1/", views.GetBorrowsBook1.as_view(), name='getBorrow1'),

    path('borrowBook/', views.BorrowBookView.as_view(), name='borrowBook'),
    path('backBook/', views.BackBookView.as_view(), name='backBook'),

    path('reservation/', views.ReservationBook.as_view(), name='reservationBook'),
    path('unReservation/<int:pk>/', views.UnReservationView.as_view(), name='unReservation'),

    path('history/<int:pk>/', views.GetHistoryView.as_view(), name='getHistory'),

    path('getReservations/', views.GetReservationListView.as_view(), name='getReservationList'),
    path('agreeReservation/', views.AgreeReservationView.as_view(), name='agreeReservation'),

    path('getBookByCategory/<int:pk>/', views.GetBooksByCategoryView.as_view(), name='getBookByCategory'),

    path('searchBook/', views.SearchBookView.as_view(), name='searchBook'),

]
urlpatterns += router.urls
