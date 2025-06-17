from django.urls import path
from .views import UploadFile
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'notes', UploadFile, basename='notes')

urlpatterns = router.urls