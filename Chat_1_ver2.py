#python Chat_1_ver2.py <name> <room> <ID>
import sys, os, thread, time, os.path

def read_chat(room_num):
	#print('Bat dau thread 1')
	time.sleep(0.5)
	while 1:
		x = os.popen('cat '+room_num).read().split('\n')[0]
		#print x
		na = x.split('/')[0]
		ro = x.split('/')[1]
		te = x.split('/')[2]
		#print(na+' said: '+te+'\t in room '+ro)

name = sys.argv[1]
room = sys.argv[2]
user = sys.argv[3]
if user == '1':
	room_pub = room+'_1'
	room_sub = room+'_2'
elif user == '2':
	room_pub = room+'_2'
	room_sub = room+'_1'

#try:
#	thread.start_new_thread( read_chat, (room_sub, ) )
#except:
#	time.sleep(1)
	#print "Error: khong the bat dau thread"

if os.path.exists(room_pub) and os.path.exists(room_sub):
	time.sleep(0.1)
	#print('Room da duoc tao');
else:
	os.system('mkfifo '+room_pub)
	os.system('mkfifo '+room_sub)

#while 1:
text = raw_input()
print(name+'/'+room+'/'+text)
	#os.system('echo '+name+'/'+room+'/'+text+' > '+room_pub)

