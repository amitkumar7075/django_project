from django.urls import path
from .views import step1_view, step2_view, step3_view, success_view

urlpatterns = [
    path('step1/', step1_view, name='step1_view'),
    path('step2/', step2_view, name='step2_view'),
    path('step3/', step3_view, name='step3_view'),
    path('success/', success_view, name='success_view'),
]
