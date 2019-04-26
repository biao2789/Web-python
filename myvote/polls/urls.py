from django.urls import path

from . import views
app_name = 'polls'
urlpatterns = [
    path('questions/', views.QuestionList.as_view()),
    path('questions/<int:pk>/', views.QuestionDetail.as_view()),
    path('choices/<int:pk>/vote/', views.VoteView.as_view()),
    path('choices/', views.ChoiceList.as_view()),
]
