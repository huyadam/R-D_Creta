import os, time, sys, thread, random
from subprocess import Popen, PIPE

check_path = False
def reg_user(room_num):
	global table
	print('Bat dau thread 1')
	time.sleep(0.5)
	while 1:
		x = os.popen('cat 000_1').read().split('\n')[0]
		#print x
		fu = x.split(',')[0]
		na = x.split(',')[1]
		ro = x.split(',')[2]
		if fu == '1':
			for pointer in range(0,5):
				if table[pointer][0] == '':
					id_user = str(pointer)
					room_pub = ro+'_'+id_user+'_p'
					room_sub = ro+'_'+id_user+'_s'
					print("room_sub: "+room_sub)
					table[pointer][0] = na
					table[pointer][1] = ro
					table[pointer][2] = room_pub
					table[pointer][3] = room_sub
					break
			print(table)
			os.system('mkfifo '+room_pub)
			os.system('mkfifo '+room_sub)
			os.system('echo '+na+','+ro+','+room_pub+','+room_sub+' > 000_2')
			print(na+','+ro+','+room_pub+','+room_sub)

def read_client():
	global table
	while 1:
		for pointer in range(0,5):
			if table[pointer][0] != '':
				txt = os.popen('cat '+table[pointer][2]).read().split('\n')[0]
				print('message come in')
				if len(txt)>2:
					#print('message come in')
					for room_gr in range(0,5):
						if table[room_gr][1] == table[pointer][1]:
							os.system('echo '+txt+' > '+table[room_gr][3])
							print('echo '+txt+' > '+table[room_gr][3])

try:
	thread.start_new_thread( read_client, ()  )
	thread.start_new_thread( reg_user, (123, ) )
except:
	print "Error: khong the bat dau thread"

table = [['','','',''],['','','',''],['','','',''],['','','',''],['','','','']]
while 1:
	time.sleep(1)
	
