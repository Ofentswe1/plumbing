from django.urls import path
from app import views

urlpatterns = [
    path('app/api/<str:username>/<str:password>/', views.Login.as_view(),
         name='login'),
    path('app/api/allbookings/', views.AllBookings.as_view(), name='allbooks'),
]
