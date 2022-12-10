from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('order_history/<order_number>',
         views.order_history,
         name='order_history'),
    path('newsletter/add/', views.add_newsletter, name='add_newsletter'),
    path('newsletter/edit/<int:newsletter_id>/', views.edit_newsletter,
         name='edit_newsletter'),
    path('newsletter/delete/<int:newsletter_id>/', views.delete_newsletter,
         name='delete_newsletter'),
]
