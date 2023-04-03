from django.urls import re_path, path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as v

urlpatterns = [
    re_path(r'^snippets/$', views.SnippetList.as_view()),
    re_path(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view()),
    re_path(r'^goods/$', views.GoodsList.as_view()),
    re_path(r'^goods/(?P<pk>[0-9]+)/$', views.GoodsDetail.as_view()),
    re_path(r'^LoginInfo/$', views.LoginUserInfo.as_view()),
    re_path(r'^users/$', views.UserList.as_view()),
    re_path(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    re_path(r'^api-token-auth/', v.obtain_auth_token)  # 生成用户token，用post，需要账号和密码，所以在登录的时候可以返回给前端
]
urlpatterns = format_suffix_patterns(urlpatterns)
