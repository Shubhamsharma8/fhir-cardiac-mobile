"""fhirheart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from django.contrib import admin

from django.conf.urls import url, include
from rest_framework import routers
from fhiradmin  import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

#router.register(r'nicotinefood', views.NicotineFoodViewSet)
router.register(r'typeofsmoke', views.TypeOfSmokeViewSet)
router.register(r'physicalactivity', views.PhysicalActivityViewSet)
router.register(r'bloodpressure', views.BloodPressureReadingViewSet)
router.register(r'dietintakeperday', views.DietInTakePerDayViewSet)
router.register(r'cholesterolreading',views.CholesterolReadingViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^myadmin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
