from django.urls import path
from rest_framework.routers import SimpleRouter  # type: ignore

from users.apps import UsersConfig
from users.views import UserViewSet, PaymentViewSet

app_name = UsersConfig.name

router = SimpleRouter()
router.register(r'users', UserViewSet, basename='users')
router.register(r'payments', PaymentViewSet, basename='payments')


urlpatterns = [] + router.urls
