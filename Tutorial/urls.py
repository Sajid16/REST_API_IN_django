from django.urls import path
from Tutorial.views import test

urlpatterns = [
    path('', test, name='blogPost'),  # in django v3 just use views name instead of views.views_name
    # path('<int:pk>/', blogPostDetails, name='details')
]
