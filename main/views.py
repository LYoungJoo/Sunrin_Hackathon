# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from datetime import datetime
from urllib import urlopen
from bs4 import BeautifulSoup

def init(request):
	Getdata.objects.create()
	return redirect('/totalgraph/')

def printdata(request):

	data = Getdata.objects.get(pk = 1)

	return render(request, 'main/arduino.html', {'data1': data.data1, 'data2' : data.data2, 
		'data3' : data.data3, 'data4': data.data4, 'data5' : data.data5, 'data6' : data.data6,
		'data7' : data.data7, 'data8': data.data8, 'data9' : data.data9, 'data10' : data.data10,
		'data11' : data.data11, 'data12': data.data12 })

def totalgraph(request):
	url = 'http://www.kpx.or.kr/www/contents.do?key=216'
	html_code = urlopen(url).read()
	bsobj = BeautifulSoup(html_code, 'html.parser')
	peakTime = bsobj.findAll('div', {'class': 'et_03'})
	peak = peakTime[0].text

	a = []
	elects = bsobj.findAll('span', {'class': 'figure'})
	for i in elects:
	    a.append(i.text)
	print a

	return render(request, 'main/totalgraph.html', {'peak' : peak , 'min' : a[1][:-7].replace(',','') , 'max' : a[0].replace(',','')})

def homegraph(request):
	## DATA ##
	data = Getdata.objects.get(pk = 1)

	## NOJIN ##
	total = data.data1 + data.data2 + data.data3 + data.data4 + data.data5
	total += data.data6 + data.data7 + data.data8 + data.data9 + data.data10
	total += data.data11 + data.data12

	if total < 100000 : 
		value = 410 + (total/1000) * 60.7
	elif total < 200000 :
		value = 910 + (total/1000) * 125.9
	elif total < 300000 :
		value = 1600 + (total/1000) * 187.9
	elif total < 400000 : 
		value = 3850 + (total/1000) * 280.6
	elif total < 500000 : 
		value = 7300 + (total/1000) * 417.7
	elif total > 500001 :
		value = 12940 + (total/1000) * 709.5
	else :
		print "ERROR"

	## max, min ##
	minv = min([data.data1, data.data2, data.data3, data.data4, data.data5, data.data6, data.data7, data.data8, data.data9, data.data10, data.data11, data.data12])
	maxv = max([data.data1, data.data2, data.data3, data.data4, data.data5, data.data6, data.data7, data.data8, data.data9, data.data10, data.data11, data.data12])

	context = {'data1': data.data1, 'data2' : data.data2, 'data3' : data.data3, 
		'data4': data.data4, 'data5' : data.data5, 'data6' : data.data6,
		'data7' : data.data7, 'data8': data.data8, 'data9' : data.data9, 
		'data10' : data.data10,'data11' : data.data11, 'data12': data.data12,
		'total' : total , 'value' : value,
		'min' : minv, 'max' : maxv}

	return render(request, 'main/homegraph.html', context)

def control(request):
	return render(request, 'main/control.html')

def nojinse(request):
	data = Getdata.objects.get(pk = 1)

	total = data.data1 + data.data2 + data.data3 + data.data4 + data.data5
	total += data.data6 + data.data7 + data.data8 + data.data9 + data.data10
	total += data.data11 + data.data12

	print total
	if total < 100000 : 
		value = 410 + (total/1000) * 60.7
	elif total < 200000 :
		value = 910 + (total/1000) * 125.9
	elif total < 300000 :
		value = 1600 + (total/1000) * 187.9
	elif total < 400000 : 
		value = 3850 + (total/1000) * 280.6
	elif total < 500000 : 
		value = 7300 + (total/1000) * 417.7
	elif total > 500001 :
		value = 12940 + (total/1000) * 709.5
	else :
		print "ERROR"

	print value

	return render(request, 'main/nojinse.html', {'value' : value})

def energy(request):
	data = Getdata.objects.get(pk = 1)

	total = data.data1 + data.data2 + data.data3 + data.data4 + data.data5
	total += data.data6 + data.data7 + data.data8 + data.data9 + data.data10
	total += data.data11 + data.data12

	sun = total/125
	bic = total/100

	return render(request, 'main/energy.html', {'sun' : sun, 'bic' : bic })


def accumulatedata(request,arduino_data):

	if datetime.today().hour == 0 or datetime.today().hour == 1:
		data = Getdata.objects.get(pk=1)
		data.data1 = int(data.data1) + int(arduino_data)
		data.save()
	elif datetime.today().hour == 2 or datetime.today().hour == 3:
		data = Getdata.objects.get(pk=1)
		data.data2 = int(data.data2) + int(arduino_data)
		data.save()
	elif datetime.today().hour == 4 or datetime.today().hour == 5:
		data = Getdata.objects.get(pk=1)
		data.data3 = int(data.data3) + int(arduino_data)
		data.save()
	elif datetime.today().hour == 6 or datetime.today().hour == 7:
		data = Getdata.objects.get(pk=1)
		data.data4 = int(data.data4) + int(arduino_data)
		data.save()
	elif datetime.today().hour == 8 or datetime.today().hour == 9:
		data = Getdata.objects.get(pk=1)
		data.data5 = int(data.data5) + int(arduino_data)
		data.save()
	elif datetime.today().hour == 10 or datetime.today().hour == 11:
		data = Getdata.objects.get(pk=1)
		data.data6 = int(data.data6) + int(arduino_data)
		data.save()
	elif datetime.today().hour == 12 or datetime.today().hour == 13:
		data = Getdata.objects.get(pk=1)
		data.data7 = int(data.data7) + int(arduino_data)
		data.save()
	elif datetime.today().hour == 14 or datetime.today().hour == 15:
		data = Getdata.objects.get(pk=1)
		data.data8 = int(data.data8) + int(arduino_data)
		data.save()
	elif datetime.today().hour == 16 or datetime.today().hour == 17:
		data = Getdata.objects.get(pk=1)
		data.data9 = int(data.data9) + int(arduino_data)
		data.save()
	elif datetime.today().hour == 18 or datetime.today().hour == 19:
		data = Getdata.objects.get(pk=1)
		data.data10 = int(data.data10) + int(arduino_data)
		data.save()
	elif datetime.today().hour == 20 or datetime.today().hour == 21:
		data = Getdata.objects.get(pk=1)
		data.data11 = int(data.data11) + int(arduino_data)
		data.save()
	elif datetime.today().hour == 22 or datetime.today().hour == 23:
		data = Getdata.objects.get(pk=1)
		data.data12 = int(data.data12) + int(arduino_data)
		data.save()
	else:
		print "ERROR"

	return HttpResponse("done!")