#!/usr/bin/env python3

f = open('<path_to_file>', 'r')
d = {}
for item in f:
	s = item.split(':')
	s[-1] = s[-1][:-1]
	if s[0] not in d:
		d[s[0]] = []
		d[s[0]].append(s[-1])
	else:
		d[s[0]].append(s[-1])
f = open('<path_to_new_file>', 'w')
for key, values in d.items():
	line = key + ' ' + ','.join(values) + '\n'
	f.write(line)