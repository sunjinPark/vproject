from django.conf.urls import patterns, include, url
from rest_framework import routers
from users import views as users_view

# from django.contrib import admin
# admin.autodiscover()

router = routers.SimpleRouter(trailing_slash=False)


router.register(r'users', users_view.UserListCreateView)
router.register(r'users', users_view.UserViewSet)
router.register(r'tokens', users_view.TokensViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'VProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    #url(r'^admin/', include(admin.site.urls)),
)
