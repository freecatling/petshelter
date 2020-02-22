from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from .views import UserView

urlpatterns =[

    url(r"^/$", UserView.as_view()),

]

urlpatterns += staticfiles_urlpatterns()
