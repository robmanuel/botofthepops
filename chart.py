# -*- coding: utf-8 -*-

import requests
import time
from random import shuffle
import random
urls=[]

for year in range (1980,1990):
	for month in range (1,13):
		for day in range (1,32,7):
			url="https://www.officialcharts.com/charts/singles-chart/%04d%02d%02d/7501/" % (year,month,day)
			urls.append(url)
		
#shuffle (urls)	

urls=["https://www.officialcharts.com/charts/singles-chart/19800108/7501/","https://www.officialcharts.com/charts/singles-chart/19800129/7501/","https://www.officialcharts.com/charts/singles-chart/19800208/7501/","https://www.officialcharts.com/charts/singles-chart/19800401/7501/","https://www.officialcharts.com/charts/singles-chart/19800415/7501/","https://www.officialcharts.com/charts/singles-chart/19800715/7501/","https://www.officialcharts.com/charts/singles-chart/19800722/7501/","https://www.officialcharts.com/charts/singles-chart/19800729/7501/","https://www.officialcharts.com/charts/singles-chart/19800808/7501/","https://www.officialcharts.com/charts/singles-chart/19800815/7501/","https://www.officialcharts.com/charts/singles-chart/19800822/7501/","https://www.officialcharts.com/charts/singles-chart/19800901/7501/","https://www.officialcharts.com/charts/singles-chart/19800915/7501/","https://www.officialcharts.com/charts/singles-chart/19800922/7501/","https://www.officialcharts.com/charts/singles-chart/19800929/7501/","https://www.officialcharts.com/charts/singles-chart/19801001/7501/","https://www.officialcharts.com/charts/singles-chart/19801008/7501/","https://www.officialcharts.com/charts/singles-chart/19801019/7501/","https://www.officialcharts.com/charts/singles-chart/19801029/7501/","https://www.officialcharts.com/charts/singles-chart/19801101/7501/","https://www.officialcharts.com/charts/singles-chart/19801108/7501/","https://www.officialcharts.com/charts/singles-chart/19801115/7501/","https://www.officialcharts.com/charts/singles-chart/19801123/7501/","https://www.officialcharts.com/charts/singles-chart/19810801/7501/","https://www.officialcharts.com/charts/singles-chart/19831201/7501/","https://www.officialcharts.com/charts/singles-chart/19860522/7501/","https://www.officialcharts.com/charts/singles-chart/19870522/7501/","https://www.officialcharts.com/charts/singles-chart/19890508/7501/"]
urls=["https://www.officialcharts.com/charts/singles-chart/19800106/7501/","https://www.officialcharts.com/charts/singles-chart/19800127/7501/","https://www.officialcharts.com/charts/singles-chart/19800203/7501/","https://www.officialcharts.com/charts/singles-chart/19800330/7501/","https://www.officialcharts.com/charts/singles-chart/19800413/7501/","https://www.officialcharts.com/charts/singles-chart/19800713/7501/","https://www.officialcharts.com/charts/singles-chart/19800720/7501/","https://www.officialcharts.com/charts/singles-chart/19800727/7501/","https://www.officialcharts.com/charts/singles-chart/19800803/7501/","https://www.officialcharts.com/charts/singles-chart/19800810/7501/","https://www.officialcharts.com/charts/singles-chart/19800817/7501/","https://www.officialcharts.com/charts/singles-chart/19800831/7501/","https://www.officialcharts.com/charts/singles-chart/19800914/7501/","https://www.officialcharts.com/charts/singles-chart/19800921/7501/","https://www.officialcharts.com/charts/singles-chart/19800928/7501/","https://www.officialcharts.com/charts/singles-chart/19800928/7501/","https://www.officialcharts.com/charts/singles-chart/19801005/7501/","https://www.officialcharts.com/charts/singles-chart/19801019/7501/","https://www.officialcharts.com/charts/singles-chart/19801026/7501/","https://www.officialcharts.com/charts/singles-chart/19801026/7501/","https://www.officialcharts.com/charts/singles-chart/19801102/7501/","https://www.officialcharts.com/charts/singles-chart/19801109/7501/","https://www.officialcharts.com/charts/singles-chart/19801123/7501/","https://www.officialcharts.com/charts/singles-chart/19810726/7501/","https://www.officialcharts.com/charts/singles-chart/19831127/7501/","https://www.officialcharts.com/charts/singles-chart/19860518/7501/","https://www.officialcharts.com/charts/singles-chart/19870517/7501/","https://www.officialcharts.com/charts/singles-chart/19890507/7501/"]
urls=["https://www.officialcharts.com/charts/singles-chart/19891231/7501/"]
for idx,url in enumerate(urls):

	print "job %d of %d" % (idx,len(urls))

	print "Request: %s" % url

	r = requests.get(url)

	print "Got: %s, Status code: %r" % (r.url,r.status_code)


	#r.text
	
	fname="%s.html" % r.url.split("/")[5]
	
	print "Filename: %s" %fname


	outF = open(fname, "w")
	outF.write(r.text.encode("utf-8"))
	outF.close()


	w=random.choice(range(1,3))

	print 
	print "waiting %d seconds..." % w
	time.sleep(w)