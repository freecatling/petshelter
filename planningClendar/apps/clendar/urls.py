from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from .views import ClendarView

urlpatterns =[

    url(r"^/$", ClendarView.as_view()),

]

urlpatterns += staticfiles_urlpatterns()
