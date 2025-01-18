from django.urls import path
from . import views
urlpatterns=[
  path('', views.electronic_list,name="electronics_list"),
  path('elecadd/', views.electronics_add,name="electronics_add"),
  path('elecedit/<int:pk>/', views.electronics_edit, name='electronics_edit'),
  path('elecdelete/<int:pk>/', views.electronics_delete, name='electronics_delete'),

  path('fashion', views.fash_list,name="fash_list"),
  path('fasadd/', views.fash_add,name="fash_add"),
  path('fasedit/<int:pk>/', views.fash_edit, name='fash_edit'),
  path('fasdelete/<int:pk>/', views.fash_delete, name='fash_delete'),

  path('grocery', views.groc_list,name="groc_list"),
  path('grocadd/', views.groc_add,name="groc_add"),
  path('grocedit/<int:pk>/', views.groc_edit, name='groc_edit'),
  path('grocdelete/<int:pk>/', views.groc_delete, name='groc_delete'),
  
]