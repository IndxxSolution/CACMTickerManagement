from django.urls import path
from .views  import *
from rest_framework_simplejwt import views as jwt_views
from rest_framework.routers import DefaultRouter



router = DefaultRouter()
router.register(r'register', Register, basename='register') 
router.register(r'dividend', Dividend, basename='dividend') 
router.register(r'dated_dividend', Dated_Dividend, basename='dated_dividend')

router.register(r'add_permission', Add_permission, basename='add_permission')
router.register(r'add_role', Add_role, basename='add_role')

router.register(r'assign_permission', Assign_permission, basename='assign_permission')
router.register(r'role_permission', Role_permission, basename='role_permission')

router.register(r'assign_role', Assign_role, basename='assign_role') 
router.register(r'user_role', User_role, basename='user_role')

router.register(r'assign_user_permission', Assign_user_permission, basename='assign_user_permission')
router.register(r'user_permission', User_permission, basename='user_permission')

router.register(r'role_user', Role_user, basename='role_user')
router.register(r'permission_role', Permission_role, basename='permission_role')
router.register(r'permission_user', Permission_user, basename='permission_user')

urlpatterns = router.urls