from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.conf.urls import url

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/new/', views.post_new, name='post_new'),
    path('cool_work', views.cool_work, name='cool_work'),
    url(r'^favicon\.ico$',RedirectView.as_view(url='/static/favicon.ico')),
]
