#!/usr/bin/env python3

#Enter the source .txt file path (could be full path or if the file is
#present in the same directory as this script, just enter the name of
#file)
path = str(input("Enter path of file : "))

#Same applies to output filename as above
new_path = str(input("Enter destination path of the new file : "))

#Editing the .txt file to format - IPs : port1, port2...
f = open(path, 'r')
d = {}
for item in f:
	s = item.split(':')
	s[-1] = s[-1][:-1]
	if s[0] not in d:
		d[s[0]] = []
		d[s[0]].append(s[-1])
	else:
		d[s[0]].append(s[-1])

#Writing to output file
f = open(new_path, 'w')
for key, values in d.items():
	line = key + ' : ' + ', '.join(values) + '\n'
	f.write(line)
