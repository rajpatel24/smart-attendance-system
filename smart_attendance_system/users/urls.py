from django.conf.urls import url, re_path
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from users.views import RegistrationAPIView

router = DefaultRouter()

urlpatterns = router.urls

urlpatterns += [
    url(r'^user/', include('rest_auth.urls')),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'rest-auth/registration/', include('rest_auth.registration.urls')),
    path('registration/', RegistrationAPIView.as_view(), name='registration')
]
