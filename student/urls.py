from django.urls import path
from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('student/<str:pk>/residence/', views.residence, name='residence'),
  path('student/<str:pk>/contact/', views.contact, name='contact'),
  path('student/<str:pk>/medical/', views.medical, name='medical'),
  path('student/<str:pk>/school/', views.school, name='school'),
  path('student/<str:pk>/game/', views.game, name='game'),
  path('student-list/', views.student_list_view, name='student-list'),
  path('student-detail/<str:pk>/', views.student_detail, name='student-detail'),
]