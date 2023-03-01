from django.urls import path
from . import views

app_name = 'markets'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.sell, name='sell'),
    path('<int:pk>/', views.detail, name='detail'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('store/<str:item_seller>/', views.store, name='store'),
]