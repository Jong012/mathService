from django.urls import path

from math_calc.views import index

urlpatterns = [
    path('', index)
]