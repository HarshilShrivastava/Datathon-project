from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name="putdata"),
    path('poi_data/', views.point_datasets, name = 'poidata'),
    path('iframe/', views.project_iframe, name='project_iframe'),
    path('comment/', views.putdata, name='comment'),
    path('comment_see', views.CommentSee, name='CommentSee'),
]