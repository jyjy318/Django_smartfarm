from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

# 경로이동
import user.views
import main.views

urlpatterns = [

    # <admin계정>
    path('admin/', admin.site.urls),

    # 로그인 <시작페이지, 로그인, 로그아웃>
    path('', user.views.index),
    path('login', user.views.login, name="login"),
    path('joinus', user.views.joinus, name='joinus'),
    path('user_insert', user.views.user_insert, name="user_insert"),
    #path('joinus', user.views.login, name="joinus"),
    
    path('index', main.views.index, name = "index"),
    path('fiindex', main.views.fiindex, name = "fiindex"),  
    path('showphoto', main.views.showphoto, name='showphoto'),
    path('tomato_givewater', main.views.tomato_givewater, name='tomato_givewater'),
    path('pepper_givewater', main.views.pepper_givewater, name='pepper_givewater'),
    path('sangcu_givewater', main.views.sangcu_givewater, name='sangcu_givewater'),
    path('predictimage', main.views.predictimage, name='predictimage'),
    path('showlive', main.views.showlive, name='showlive'),
    path('logout', main.views.logout, name='logout'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
