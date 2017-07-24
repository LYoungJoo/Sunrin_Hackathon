from django.conf.urls import url,include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$',views.init),
	url(r'^printdata/$',views.printdata),
	url(r'^homegraph/$',views.homegraph),
	url(r'^totalgraph/$',views.totalgraph),
	url(r'^nojinse/$',views.nojinse),
	url(r'^energy/$',views.energy),
	url(r'^control/$',views.control),
	url(r'^arduino/(?P<arduino_data>.+)', views.accumulatedata),

]
