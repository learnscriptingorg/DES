from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    # path('',views.load_build,name='load_build'),

]
