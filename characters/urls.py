from django.urls import path
from . import views

urlpatterns = [
    path('', views.character_list, name='characters'),
    path('<slug:category_slug>/', views.character_list, name='characters_by_category'),
    path('<int:id>/<slug:slug>/', views.character_detail, name='character_detail'),
    path('', views.character_add, name='character_add'),
    path('<int:id>', views.character_edit, name='character_edit'),
]
