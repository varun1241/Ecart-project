from django.urls import path


from .views import CollegeView,CollegeUpadteView


urlpatterns = [

    path('college/',CollegeView.as_view(),name="college"),
    
    path('college/<int:pk>/',CollegeUpadteView.as_view(),name="collegeupdate")
]