from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    # path('site1/', include('site1.urls')),
    path('poll/', include('poll.urls')),
]