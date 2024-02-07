from rest_framework.routers import SimpleRouter

from .views import (
    NotificationViewSet
)


router = SimpleRouter()
router.register("notification", NotificationViewSet)
urlpatterns = router.urls