from django.urls import path
from Content.views import contentList


urlpatterns = [
    path('', contentList, name = 'contentList'),   # in django v3 just use views name instead of views.views_name
]
