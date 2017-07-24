# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from datetime import datetime

ck = 0

def index(request):
	return render(request, 'main/index.html')

def printdata(request):
	#check model
	global ck
	if ck == 0:
		Getdata.objects.create()
		ck = 1

	data = Getdata.objects.get(pk = 1)

	return render(request, 'main/arduino.html', {'data1': data.data1, 'data2' : data.data2, 
		'data3' : data.data3, 'data4': data.data4, 'data5' : data.data5, 'data6' : data.data6,
		'data7' : data.data7, 'data8': data.data8, 'data9' : data.data9, 'data10' : data.data10,
		'data11' : data.data11, 'data12': data.data12 })

def accumulatedata(request,arduino_data):

	if datetime.today().hour == 0 or datetime.today().hour == 1:
		data = Getdata.objects.get(pk=1)
		print data.data1
		print arduino_data
		print datetime.today().hour
		data.data1 = int(data.data1) + int(arduino_data)
		data.save()
	elif datetime.today().hour == 2 or datetime.today().hour == 3:
		data = Getdata.objects.get(pk=1)
		data.data2 = data.data2 + arduino_data
		data.save()
	elif datetime.today().hour == 4 or datetime.today().hour == 5:
		data = Getdata.objects.get(pk=1)
		data.data3 = data.data3 + arduino_data
		data.save()
	elif datetime.today().hour == 6 or datetime.today().hour == 7:
		data = Getdata.objects.get(pk=1)
		data.data4 = data.data4 + arduino_data
		data.save()
	elif datetime.today().hour == 8 or datetime.today().hour == 9:
		data = Getdata.objects.get(pk=1)
		data.data5 = data.data5 + arduino_data
		data.save()
	elif datetime.today().hour == 10 or datetime.today().hour == 11:
		data = Getdata.objects.get(pk=1)
		data.data6 = data.data6 + arduino_data
		data.save()
	elif datetime.today().hour == 12 or datetime.today().hour == 13:
		data = Getdata.objects.get(pk=1)
		data.data7 = data.data7 + arduino_data
		data.save()
	elif datetime.today().hour == 14 or datetime.today().hour == 15:
		data = Getdata.objects.get(pk=1)
		data.data8 = data.data8 + arduino_data
		data.save()
	elif datetime.today().hour == 16 or datetime.today().hour == 17:
		data = Getdata.objects.get(pk=1)
		data.data9 = data.data9 + arduino_data
		data.save()
	elif datetime.today().hour == 18 or datetime.today().hour == 19:
		data = Getdata.objects.get(pk=1)
		data.data10 = data.data10 + arduino_data
		data.save()
	elif datetime.today().hour == 20 or datetime.today().hour == 21:
		data = Getdata.objects.get(pk=1)
		data.data11 = data.data11 + arduino_data
		data.save()
	elif datetime.today().hour == 22 or datetime.today().hour == 23:
		data = Getdata.objects.get(pk=1)
		data.data12 = data.data12 + arduino_data
		data.save()
	else:
		print "ERROR"

	return HttpResponse("done!")