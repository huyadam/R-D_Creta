import os, time, sys, thread, random
from subprocess import Popen, PIPE

check_path = False
def reg_user(room_num):
	print('Bat dau thread 1')
	time.sleep(0.5)
	while 1:
		x = os.popen('cat 000_1').read().split('\n')[0]
		#print x
		fu = x.split(',')[0]
		na = x.split(',')[1]
		ro = x.split(',')[2]
		if fu == '1':
			id_user = str(random.randint(1,1000))
			room_pub = ro+'_'+id_user+'_p'
			room_sub = ro+'_'+id_user+'_s'
			if os.path.exists(room_pub) and os.path.exists(room_sub):
				print('Room da duoc tao');
			else:
				os.system('mkfifo '+room_pub)
				os.system('mkfifo '+room_sub)
			os.system('echo '+na+','+ro+','+room_pub+','+room_sub+' > 000_2')
			print(na+','+ro+','+room_pub+','+room_sub)


try:
	thread.start_new_thread( reg_user, (123, ) )
except:
	print "Error: khong the bat dau thread"

while 1:
	time.sleep(1)
	