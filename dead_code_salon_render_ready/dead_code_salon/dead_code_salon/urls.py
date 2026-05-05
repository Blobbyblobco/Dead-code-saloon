from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('draw/', views.draw_duel, name='draw_duel'),
    path('fight/', views.fight_betting, name='fight'),
]
