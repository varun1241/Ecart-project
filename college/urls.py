from django.urls import path,include


from .views import CollegeView,CollegeUpadteView

from .router import router
from rest_framework.authtoken import views

urlpatterns = [

    path('college/',CollegeView.as_view(),name="college"),
    
    path('college/<int:pk>/',CollegeUpadteView.as_view(),name="collegeupdate"),
    
    path('api/', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]