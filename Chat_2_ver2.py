import os, time, sys, thread
from subprocess import Popen, PIPE

check_path = False
def read_chat(room_num):
	print('Bat dau thread 1')
	time.sleep(0.5)
	while 1:
		x = os.popen('cat '+room_num).read().split('\n')[0]
		#print x
		na = x.split('/')[0]
		ro = x.split('/')[1]
		te = x.split('/')[2]
		print(na+' said: '+te+'\t in room '+ro)


a = os.popen('python Chat_1_ver2.py Tuan 934 2').read().split('\n')[0]
nam = a.split('/')[0]
roo = a.split('/')[1]
tex = a.split('/')[2]

os.system('echo 1,'+nam+','+roo+' > 000_1')

while 1:
	if check_path:
		#print('check_path is ok')
		a = os.popen('python Chat_1_ver2.py Tuan 934 2').read().split('\n')[0]
		print('said: '+a) 
		#os.system('echo '+name+'/'+room+'/'+text+' > '+room_pub)
		#time.sleep(1)
	elif len(a) > 2:
		a = os.popen('cat 000_2').read().split('\n')[0]  
		#mess_recv: <name>,<room>,<room_pub>,<room_sub>
		print a
		if a.split(',')[0] == nam and a.split(',')[1] == roo:
			room_pub = a.split(',')[2]
			room_sub = a.split(',')[3]
			try:
				thread.start_new_thread( read_chat, (room_sub, ) )
			except:
			   print "Error: khong the bat dau thread"
			a = ''
			check_path = True
	
