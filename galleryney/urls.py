"""
URL configuration for galleryney project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accounting.urls')),
    path('', include('affiliates.urls')),
    path('', include('authentication.urls')),
    path('', include('blogs.urls')),
    path('', include('caching.urls')),
    path('', include('calculator.urls')),
    path('', include('certainaccounts.urls')),
    path('', include('common.urls')),
    path('', include('configuration.urls')),
    path('', include('connectedservices.urls')),
    path('', include('customers.urls')),
    path('', include('discounts.urls')),
    path('', include('estates.urls')),
    path('', include('events.urls')),
    path('', include('exportimport.urls')),
    path('', include('financialyear.urls')),
    path('', include('forums.urls')),
    path('', include('helpers.urls')),
    path('', include('home.urls')),
    path('', include('localization.urls')),
    path('', include('loging.urls')),
    path('', include('mediahelpers.urls')),
    path('', include('messages.urls')),
    path('', include('news.urls')),
    path('', include('orders.urls')),
    path('', include('payments.urls')),
    path('', include('plugins.urls')),
    path('', include('polls.urls')),
    path('', include('scheduletasks.urls')),
    path('', include('security.urls')),
    path('', include('seo.urls')),
    path('', include('shipping.urls')),
    path('', include('stores.urls')),
    path('', include('tax.urls')),
    path('', include('tests.urls')),
    path('', include('themes.urls')),
    path('', include('topics.urls')),
    path('', include('treasury.urls')),
    path('', include('vendors.urls')),
    path('', include('warehousemanagement.urls')),
    path('', include('warehouses.urls')),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
