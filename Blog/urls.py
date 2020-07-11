from django.urls import path
from Blog.views import blogPosts, blogPostDetails


urlpatterns = [
    path('', blogPosts, name = 'blogPost'),   # in django v3 just use views name instead of views.views_name
    path('details/<int:pk>/', blogPostDetails, name='details')
]
