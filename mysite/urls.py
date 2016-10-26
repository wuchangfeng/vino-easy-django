from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # 默认管理员的 admin
    url(r'^admin/', include(admin.site.urls)),
    # ，Django 会把访问 'http://127.0.0.1:8000/' 的请求
    # 转到 blog.urls，并看看那里面有没有进一步的指示。
    url(r'', include('blog.urls')),
]