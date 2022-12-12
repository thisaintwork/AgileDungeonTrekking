from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.character_list, name='characters'),
    path('<slug:category_slug>/', views.character_list, name='characters_by_category'),
    path('detail/<int:id>', views.character_detail, name='character_detail'),
    path('create', views.character_add, name='character_add'),
    path('modify/<int:id>', views.character_modify, name='character_modify'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
