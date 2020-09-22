from rest_framework import routers
from pizza.viewsets import PizzaViewSet, LikeViewSet


router = routers.DefaultRouter()

router.register(r'api/v1/pizza', PizzaViewSet)
router.register(r'api/v1/like', LikeViewSet)

urlpatterns = router.urls
