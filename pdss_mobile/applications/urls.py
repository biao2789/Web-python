from django.urls import path
from . import views
from django.views.static import serve

app_name = 'applications'
urlpatterns = [
    path('apps/', views.AppList.as_view()),
    path('apps/latest/', views.AppLatest.as_view()),
]
