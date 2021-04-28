from django.urls import path, include
from authe.views import RegisterView, ChangePasswordView , UpdateInfoView, LogOutView #, MyTokenObtainPairView 
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView, TokenObtainPairView




urlpatterns = [
   path('login/',TokenObtainPairView.as_view()),
   # path('login/', MyTokenObtainPairView.as_view()),
   path('login/refresh/', TokenRefreshView.as_view()),
   path('login/verify/', TokenVerifyView.as_view()),
   path('register/',RegisterView.as_view()),
   path('changepassword/<int:pk>/', ChangePasswordView.as_view()),
   path('updateinfo/<int:pk>/', UpdateInfoView.as_view()),
   path('logout/', LogOutView.as_view(), ),
   
]