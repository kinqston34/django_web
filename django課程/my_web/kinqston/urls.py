from django.urls import path
from . import views

urlpatterns = [
    path('',views.base,name="Base"),
    path('customer/',views.index,name="Index"),
    path('customer/update/<str:pk>',views.update,name='Update'),
    path('customer/delete/<str:pk>',views.delete,name='Delete'),
    path('customer/communication/<str:pk>',views.communication,name="Communication"),
]