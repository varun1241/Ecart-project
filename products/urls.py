

from django.urls import path, re_path
from .views import HomePage,Login,Singup,logout,Cart,ProductView,TaskCreateView,TaskUpdateView,ProductDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/',HomePage.as_view(),name='home'),
 path('',Login.as_view(),name='login'),
  path('signup/',Singup.as_view(),name='signup'),
  path('logout',logout,name='logout'),
   path('cart/',Cart.as_view(),name='cart'),
    path('product-view/',ProductView.as_view(),name='product-view'),
   path('create/', TaskCreateView.as_view(), name='task_create'),
   path('update/<int:pk>/',TaskUpdateView.as_view(), name='task_update'),
    path('delete/<int:pk>/',ProductDeleteView.as_view(), name='task_delete'),
]

if settings.DEBUG:
  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
