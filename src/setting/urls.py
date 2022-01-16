from django.urls import path
from . import views


app_name='setting'

urlpatterns=[
    path('', views.Home ,name='Home'),
    path('contact/', views.contact ,name='contact'),
    path('<int:pk>', views.itemDetails.as_view() , name='itemDetails'),

    
]

