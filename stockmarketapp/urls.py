from django.urls import path
from . import views

app_name = 'Stockapp'

urlpatterns = [
    path('stockdetailapicall/', views.stockdetailapicall,
         name="stockdetailapicall"),
    path('index/', views.indexpage, name="indexpage"),
]
