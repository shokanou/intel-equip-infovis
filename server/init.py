import os
import sys
import string,re

colon = ":"
#usr_id = []

def open_txt(file = "test_id.txt"):
	try:
		data = open(file)
		return file
	except Exception,e:
		print str(e)

def get_id(file="test_id.txt"):
	usr_id = []
	data = open(file,'r')
	for line in open(file):
		line = data.readline()
		if line != '\n':
			line = line.split(colon)
		#print line
			tmp = line[1]
			tmp_id = tmp[2:13]
			usr_id.append(tmp_id)

	data.close()

	return usr_id

def main():
	usr_id = get_id()

if __name__=="__main__":
    main()


