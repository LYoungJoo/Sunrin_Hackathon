from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$',views.index),
	url(r'^printdata/$',views.printdata),
	url(r'^arduino/(?P<arduino_data>.+)', views.accumulatedata),

]
