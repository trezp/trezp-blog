from django.urls import path 

from . import views 

urlpatterns = [
  # path('', views.BlogListView.as_view(), name='home'),
  path('', views.LogListView.as_view(), name="home"),
  path('<int:pk>/', views.LogDetailView.as_view(), name="log_detail"),
  path('post/<int:pk>/', views.BlogDetailView.as_view(), name='post_detail'),
  path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
  path('post/<int:pk>/edit/', views.BlogUpdateView.as_view(), name='post_edit'),
  path('post/<int:pk>/delete/', views.BlogDeleteView.as_view(), name='post_delete')
]