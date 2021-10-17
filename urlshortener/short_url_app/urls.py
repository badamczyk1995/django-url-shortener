from django.urls import path
from . import views

app_name = 'short_url_app'

urlpatterns = [
    path('', views.short_url_view, name='home'),
    path('<str:short_url>', views.redirect_view, name='redirect'),
]
