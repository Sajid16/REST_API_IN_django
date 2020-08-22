from django.urls import path
from .views import tutorial_list, tutorial_detail, tutorial_list_published

urlpatterns = [
    path('', tutorial_list),
    path('<int:pk>/', tutorial_detail),
    path('published/', tutorial_list_published)
]
