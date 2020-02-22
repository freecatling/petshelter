from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import url
from .views import PlanView

urlpatterns =[

    url(r"^/$", PlanView.as_view()),

]

urlpatterns += staticfiles_urlpatterns()
