from django.urls import path

from . import views
app_name = 'matching'

urlpatterns = [
    path('', views.PostListView.as_view(), name="home"),
    path('create_post/', views.PostCreateView.as_view(), name='create_post')

]