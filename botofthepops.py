# -*- coding: utf-8 -*-

import os.path
import datetime
import sys
import urllib
from datetime import timedelta



now = datetime.datetime.now()


if len(sys.argv)>1:
	hit=int(sys.argv[1])
	override=True
else:
	hit=40
	override=False


if len(sys.argv)>2:
	year=int(sys.argv[2])
else:
	yearprefix="198"
	year=int(yearprefix+str(now.year)[3])
	

def nearestDate(now):
	#year=int(yearprefix+str(now.year)[3])
	roughdate= datetime.date(year,now.month,now.day)
	nextsun=6-roughdate.weekday()
	chartdate=roughdate+timedelta(days=nextsun)
	chartdate=chartdate-timedelta(days=7)
	z="%04d%02d%02d" % (chartdate.year, chartdate.month, chartdate.day)
	return z

def processEntry(d):
	ret={}
	d=d.split("\t")	
	
	if "N" in d[2]:
		d[2]="0"
	elif "R" in d[2]:
		d[2]="-100"


	ret={
	"weekid":int(d[0]),
	"position":int(d[1]),
	"lastweek":int(d[2]),
	"artist":d[3].rstrip(),
	"title":d[4].rstrip(),
	"label":d[5].rstrip(),
	"peak":int(d[6]),
	"weeks":int(d[7]),
	"chartid":d[8].rstrip(),
	"productid":d[9].rstrip()
	}
	
	return ret
	
	
def makeEmoji(d):
	if d["position"]<d["lastweek"]:
		icon="⬆️"
		text="Climbing to %s from %s" % (d["position"],d["lastweek"])
	if d["position"]>d["lastweek"]:
		icon="⬇️"
		text="Dropping to %s from %s" % (d["position"],d["lastweek"])
	if d["position"]==d["lastweek"]:
		icon="🔄"
		text="A non-mover at %s" % d["position"]
	if d["lastweek"]==-100:
		icon="↪️"
		text="A non-mover at %s" % d["position"]
	if d["lastweek"]==-0:
		icon="🆕"
		text="A new entry at %s" % d["position"]

	return icon,text

# nearestDate(datetime.date(1980,1,1))

data="charts1980s.txt"






d=[]
text_file = open(data, "r")
lines = text_file.readlines()
text_file.close()


z=nearestDate(datetime.datetime.now())

#does chart position file exist?

if override==False:
	chartfile=z+".txt"

	if os.path.exists(chartfile):
		print "%s exists" % chartfile
	else:
		#if not create it with value 40
		print "%s does not exist" % chartfile
		f=open(chartfile,"w")
		f.write(str(hit))
		f.close()


	#read chart position

	f=open(chartfile,"r")
	hit=int(f.read())
	f.close()

	#write chart position
	f=open(chartfile,"w")
	f.write(str(hit-1))
	f.close()





for l in lines:
	
	if z in l:
		d=processEntry(l)
		if d["position"]==hit:
			emoji,text = makeEmoji(d)
			yturl="http://www.google.com/search?q=youtube+%s+%s&btnI" % (urllib.quote(d["artist"]),urllib.quote(d["title"]).split("/")[0])
			wikiurl="http://www.google.com/search?q=wiki+%s+%s&btnI" % (urllib.quote(d["artist"]),urllib.quote(d["title"]).split("/")[0])
			out="%s\n\n%s %s %s - %s\n\nYouTube: %s\nWikipedia: %s" % (text+" this week in "+now.strftime("%B")+" "+str(year),emoji,d["position"],d["artist"],d["title"],yturl,wikiurl)
			print out