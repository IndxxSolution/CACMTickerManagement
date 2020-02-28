from django.urls import path
from .views  import Register, Dividend
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'register', Register, basename='register') 
router.register(r'dividend', Dividend, basename='dividend') 
urlpatterns = router.urls