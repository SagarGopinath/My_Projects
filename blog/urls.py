from django.urls import path
from .views import Homeview , Articleview , Addpost,UpdatePost,DeletePost,CategoryView

urlpatterns = [
    path('',Homeview.as_view(),name='home'),
    path('article/<int:pk>',Articleview.as_view(),name='article'),
    path('addpost/',Addpost.as_view(),name='addpost'),
    path('article/edit/<int:pk>',UpdatePost.as_view(),name = "update"),
    path('article/delete/<int:pk>',DeletePost.as_view(),name = "delete"),
    path('category/<str:cats>/',CategoryView,name='category')

]