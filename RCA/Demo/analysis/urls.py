from django.urls import path
from . import views
urlpatterns=[

    path('load_build',views.load_build,name='load_build'),
    path('',views.index,name='index'),
]
