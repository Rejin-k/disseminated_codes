import os
import sys

import zipfile
import uuid 

def generateUUID():
    return str(uuid4())
path = raw_input("Enter folder path you want to zip :")
if os.path.exists(path):
	print ("path",path,"exists")
	list_a=os.listdir(path)
	count =1000
	print(len(list_a))
	new_list=[]
	for i in range(len(list_a)):
		new_list.append(path+'/'+list_a[i])
		if i == count:
			with zipfile.ZipFile('reportDir' + str(uuid.uuid4()) + '.zip', 'w') as myzip:
			    for f in new_list:   
				myzip.write(f)
			new_list=[]
			count=count+1000
else:
	print("Directory doest exist")
