from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from bikes4FreeApp import views
from bikes4FreeApp.views import ComboViewSet, DishViewSet, IngredientViewSet, BeverageViewSet

router = DefaultRouter()
router.register(r'combos', ComboViewSet)
router.register(r'dishes', DishViewSet)
router.register(r'ingredients', IngredientViewSet)
router.register(r'beverages', BeverageViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]

#urlpatterns =format_suffix_patterns(urlpatterns)
urlpatterns += router.urls
