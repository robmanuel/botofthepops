# -*- coding: utf-8 -*-

import json
from pprint import pprint
import glob


files=glob.glob("*.xml")

for f in files:
	with open(f) as data_file:    
		data = json.load(data_file)
	#pprint(data)

	#data['Chart_Runs'][0]['Runs'][0]['Position']

	score=0
	for r in data['Chart_Runs'][0]['Runs']:
		score+=101-int(r['Position'])

	if 	int (data['Peak_Position'])>40:
		print data['Artist_Name'].encode("utf-8"),"\t",
		print data['Product_Name'].encode("utf-8"),"\t",
		print data['Peak_Position'].encode("utf-8"),"\t",
		print score