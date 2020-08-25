from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import snippet_list, snippet_detail
from .views import SnippetList, SnippetDetail

urlpatterns = [
    path('', snippet_list),
    path('<int:pk>/', snippet_detail),
    path('class-based-view/', SnippetList.as_view()),
    path('class-based-view/<int:pk>/', SnippetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
