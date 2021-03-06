"""rugbyshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts.views import index
from accounts import urls as accounts_urls
from products import urls as urls_products
from cart import urls as urls_cart
from search import urls as urls_search
from checkout import urls as urls_checkout
from products.views import all_products
from home import urls as urls_home
from home.views import contact
from review import urls as urls_review
from review.views import get_review
from posts import urls as urls_posts
from posts.views import get_posts
from django.views import static
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^products/', include(urls_products)),
    url(r'^products/', all_products, name='all_products'),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^review/', include('review.urls')),
    url(r'^review/', include(urls_review)),
    url(r"^review$", get_review, name="get_review"),
    url(r'^posts/', include('posts.urls')),
    url(r'^posts/', include(urls_posts)),
    url(r"^posts$", get_posts, name="get_posts"),
    url(r'^search/', include(urls_search)),
    url(r'^home/', include(urls_home)),
    url(r'^contact/', contact, name='contact'),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
]
