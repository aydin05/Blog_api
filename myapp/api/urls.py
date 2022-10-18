from django.conf.urls import url
from myapp.api.views import BlogAPIView

urlpatterns = [
    url('post', BlogAPIView.as_view()),
]
