from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name='index'),
    path('manage', views.manage , name='manage'),
    path('success', views.success, name='success'),
    path('delete/<int:id>', views.delete , name='delete'),
    path('update/<int:id>', views.update , name='update'),
]