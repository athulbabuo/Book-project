from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [

      path("",views.CreateBook),
      path('listview/',views.listBook),
      path('detailsview/<int:book_id>/',views.detailsView,name='details'),
      path('updateview/<int:book_id>/',views.updateBook,name='update'),
      path('deleteview/<int:book_id>/',views.deleteBook,name='delete'),

]
