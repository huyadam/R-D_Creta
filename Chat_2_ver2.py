import os, time, sys, thread
from subprocess import Popen, PIPE

check_path = False
def read_chat(room_num):
	print('Bat dau thread 1')
	time.sleep(0.5)
	while 1:
		x = os.system('cat '+room_num)

def read_path():
	print('Bat dau thread 2')
	time.sleep(0.5)
	while 1:
		x = os.system('cat 000_2')

name = sys.argv[1]
room = sys.argv[2]
pipe_reg_send = sys.argv[4]
pipe_reg_recv = sys.argv[3]

retval = os.system('echo 1,'+name+','+room+' > 000_1')
while 1:
	a = os.popen('cat 000_2').read().split('\n')[0]
	print a
	if len(a) > 2:
		room_pub = a.split(',')[0]
		room_sub = a.split(',')[1]
		try:
			thread.start_new_thread( read_chat, (room_sub, ) )
		except:
		   print "Error: khong the bat dau thread"

		while 1:
			retval = os.system('python Chat_1.py '+name+' '+room+' > '+room_pub)
			#print retval
			if retval == 2 or retval == 256:
				retval = os.system('echo 0,'+name+','+room+' > 000_1')
				sys.exit(0)
			#time.sleep(1)
	
