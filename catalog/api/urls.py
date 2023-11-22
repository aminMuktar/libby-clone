from rest_framework.routers import DefaultRouter

from catalog.api.views import AuthorViewSet, BookViewSet

router = DefaultRouter()
app_name = 'catalog-api'


router.register(r'authors', AuthorViewSet)
router.register(r'books', BookViewSet)
urlpatterns = router.urls
