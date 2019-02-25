# -*- coding: utf-8 -*-

# GREP to reduce it down
# grep 1984[0-9][0-9][0-9][0-9] charts1980.txt > charts1984.txt
# 
# AWK to get greater > 40
# awk -F$'\t' ' $7>40' charts1984.txt
#
# get list of ids
#awk 'NF{print $NF}' flops84.txt | uniq > sing.txt
#
# final list
# python jason.py | sort -n -r -t$'\t' -k4 | cat -n



from bs4 import BeautifulSoup
import re
import glob

def filetodata(fname):
	f = open(fname, "r")
	html=f.read()
	soup = BeautifulSoup(html, 'html.parser')

	position=soup.find_all("span",class_="position")
	lastweek=soup.find_all("span",class_="last-week")
	artist=soup.find_all("div",class_="artist")
	title=soup.find_all("div",class_="title")
	label=soup.find_all("span",class_="label")
	chartid=soup.find_all("a", class_="chart-runs-icon")
	productid=soup.find_all("a", class_="chart-runs-icon")

	xx=html.replace("\n","")
	xx=xx.replace("\t","")
	peak=re.findall(r'<!-- Peak Position-->        <td>(.*?)</td>',xx)
	weeks=re.findall(r'<!-- Wks -->        <td>(.*?)</td>',xx)




	for p,l,a,t,lb,pk,w,c,pid in zip(position,lastweek,artist,title,label,peak,weeks,chartid,productid):
		print fname.split(".")[0].encode("utf-8"),"\t",
		print p.text.strip().encode("utf-8"),"\t",
		print l.text.strip().encode("utf-8"),"\t",
		print a.text.strip().encode("utf-8"),"\t",
		print t.text.strip().encode("utf-8"),"\t",
		print lb.text.strip().encode("utf-8"),"\t",
		print pk.encode("utf-8"),"\t",
		print w.encode("utf-8"),"\t",
		print c.attrs["data-chartid"].encode("utf-8"),"\t",
		print pid.attrs["data-productid"].encode("utf-8"),"\t"

	
files=glob.glob("*.html")

files.sort()

for file in files:
	filetodata (file)