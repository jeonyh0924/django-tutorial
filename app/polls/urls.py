from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # r'^&'
    path('<int:question_id>/', views.detail, name='detail'),
    # r'^(?P<question_id>\d+)/$
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
