#!/usr/bin/env python
import sys
for line in sys.stdin:
	words = line.split()
	for word in words:
		word = ''.join(ch for ch in word if ch.isalnum()).lower()
		print('{0}\t{1}'.format(word, 1))