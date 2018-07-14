import os, time, sys, thread
from subprocess import Popen, PIPE

while 1:
	a = os.popen('python Chat_1_ver2.py Tuan 934 2').read().split('\n')[0] 
	print('said: '+a)
	
