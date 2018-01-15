import os.path
import os
import platform
import commands
import time
import uuid
import sys
import urllib2, urllib
import atexit
import socks
import socket
import socket
import select
os.system('clear')
print "Welcome to pseudo V0.2"
print "                              _"       
print "	                     | |"       
print "_ __   ___   ___  _   _   __ | |  ___ "
print "| '_ \ / __| / _ \| | | | / _` | / _ \ "
print "| |_) |\__ \|  __/| |_| || (_| || (_) |"
print "| .__/ |___/ \___| \__,_| \__,_| \___/ "
print "| |"                                    
print "|_|"                      
global cwd
global version
global uid
version = "0.2"
prompt = ''
path = '/var/tmp/uid.txt'
time.sleep(1)
ufile = os.path.exists(path)
# torify connection 
print "torifying connection \r"
print "\r"
try: 
	socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS4, '127.0.0.1', 9050, True)
	socket.socket = socks.socksocket
	ip = urllib2.urlopen("https://icanhazip.com").read()
	print "Current IP used: " + ip
except socket.error, (value,message):
    if s:
        s.close()
    	print "Could not open tor connection: " + message 
	print "\r"
	time.sleep(2)
	print "your connection is not torified"
	print "\r" 

# check for updates 
def check_version():
	fp = urllib2.urlopen("http://www.example.com/version.txt")
	currentversion = fp.read()
	if (currentversion > version):
		print "a new update is available \n"
		com = raw_input("would you like to download it (yes or no) > ")
		com_array = ['yes', 'no']
		search = com in com_array
		if (search == False):
			print "\r"
			com = raw_input("would you like to download it (yes or no) > ")
		if not com:
			 print "\r"
			 com = raw_input("would you like to download it (yes or no) > ")
		if (com == "yes"):
			download_update()
 
def download_update():
	url = "http://www.example.com/pseudo.tar.gz"
	file_name = url.split('/')[-1]
	u = urllib2.urlopen(url)
	f = open(file_name, 'wb')
	meta = u.info()
	file_size = int(meta.getheaders("Content-Length")[0])
	print "Downloading:   %s   Bytes:   %s  " % (file_name, file_size)
	file_size_dl = 0
	block_sz = 8192
	while True:
    		buffer = u.read(block_sz)
    		if not buffer:
        		break

    		file_size_dl += len(buffer)
    		f.write(buffer)
    		status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
    		status = status + chr(8)*(len(status)+1)
    		print status  
	f.close()
	commands.getoutput("tar -xvf pseudo.tar.gz")
	print "\r"
	com = raw_input("restart program to update (yes or no)")
	com_array = ['yes', 'no']
	search = com in com_array
	if (search == False):
		print "\r"
		com = raw_input("restart program to update (yes or no)")
	if not com:
		print "\r"
		com = raw_input("restart program to update (yes or no)")
	if (com == "yes"):
	        restart_program()

# at exit run these cleanup functions
def premexit():
	os.system('clear')
        log_user_out()

# runs the function above on premature termination 
atexit.register(premexit)	

# restart program after generating uid
def restart_program():
	python = sys.executable
	os.execl(python, python, * sys.argv)
        
# check if the userid file exist
def checkuid(ufile):
	if (ufile == False):
		generateuid()
	if (ufile == True):
		check_version()
		loginuser()

# generate a uid for the user
def generateuid():
	global uid
	uid = uuid.uuid1()
	f = open('uid.txt','w')
	f.write(str(uid))
	f.close()
        commands.getoutput("sudo mv uid.txt  /var/tmp/uid.txt")
	commands.getoutput("rm uid.txt")
        cpname = platform.node()
	print "your ID number is: " + str(uid)
	print "\r"
	print "please enter a name to be identified by"
        username = raw_input(prompt)
	mydata=[('uid',uid), ('comp', cpname), ('username', username)]
	mydata=urllib.urlencode(mydata)
	path='http://www.example.com/start.php'
	req=urllib2.Request(path, mydata)
	req.add_header("Content-type", "application/x-www-form-urlencoded")
	response=urllib2.urlopen(req).read()
	if (response != "successful"):
			# print response 
			print "Server Error Please Contact Server Owner"
			commands.getoutput("sudo rm /var/tmp/uid")
                	exit()
	if (response == "successful"):
			# print response
        		time.sleep(3)
			restart_program()

# found the uid file login user
def loginuser():
 	global uname
	f = open('/var/tmp/uid.txt','r')
	uid = f.read()
	cpname = platform.node()
        print "\r"
	print "\r"
	print "please wait while we verify your account..."
	time.sleep(2)
	mydata=[('uid',uid), ('comp', cpname)]
	mydata=urllib.urlencode(mydata)
	path='http://www.example.com/verify.php'
	req=urllib2.Request(path, mydata)
	req.add_header("Content-type", "application/x-www-form-urlencoded")
	print "\r"
	response=urllib2.urlopen(req).read()
	
	# no response was returned
	if not response:
		print "sorry we could not verify your account, please try again"
		exit()

	# this response means it was not found in the database
	if (response == "failed"):
		print "Sorry no account was found, please wait we will generate a new one"
		commands.getoutput("sudo rm /var/tmp/uid.txt")
		restart_program()

	# we got a good response the user has been verified 
	if response:
		time.sleep(1)
		uname = response
		print "account verified, please wait...."
		time.sleep(2)
                startit = True 
		os.system('clear')
		programstart(uname)

# get username 
def getusername():
	f = open('/var/tmp/uid.txt','r')
	uid = f.read()
	cpname = platform.node()
	mydata=[('uid',uid), ('comp', cpname)]
	mydata=urllib.urlencode(mydata)
	path='http://www.example.com/verify.php'
	req=urllib2.Request(path, mydata)
	req.add_header("Content-type", "application/x-www-form-urlencoded")
	response=urllib2.urlopen(req).read()
	if (response == "failed"):
		exit()
	if not response:
		print "sorry we could not verify your account, please try again"
		exit()
	if response:
		uname = response

# start main program
def programstart(uname):	
	print "Welcome " + uname + "\r"
	print "\r"
	print " ============ Commands List ================\r"
	print " |          help    (commands list)         | \r"
	print " |          private (private messages)      | \r"
 	print " |          members (members list by alias) | \r"
	print " |          online  (online users)          |  \r" 
	print " |          message (message board) 	    | \r"
	print " |          live    (live chat)             | \r"
	print " |          exit    (exit program)          | \r" 
	print " |==========================================| \r"
	print " \r"
	com = raw_input("please enter your command > ")
	command(com)

# command requst
def command(com):
	commandlist(com)

# command line 
def commandline(com):
	commandlist(com)

# =============================
# 
#    Commands list  
#
# =============================

# Master Commands list 
def commandlist(list):
	
	#commands array 
	com_array = ['h', 'help', 'private','members','online','message','live', 'clear', 'exit', 'restart']
        # search the array for requested command 
        search = list in com_array
        
        # can't find command warn user and drop them to command line
	if (search == False):
		print "\r"
		com = raw_input("command not found, please try again > ")
		commandline(com)
	else:
        	# command was found now let them run it 
		
	        # help command 
		if (list == "h"):
			command_help()

		# same as above 
		if (list == "help"):
			command_help()
		
		# exit program 
                if (list == "exit"):
			command_exit()

		# clear screen drop back to cmdline
		if (list == "clear"):
			os.system('clear')
			programstart(uname)

		# online users 
		if (list == "online"):
			online_users()

                # members directory 
		if (list == "members"):
                    	members_directory()
			
                # TODO ITEMS LISTED HERE!
		if (list == "private"):
	          	private_messages()

	        if (list == "message"):
	          	print "sorry this item is not done yet"
			com = raw_input(prompt)
			commandline(com)

		if (list == "live"):
			
	        	chat_client()
		

                if (list == "restart"):
			restart_program()
	
        	# prevent program from exiting on blank line
		if not list:
			com = raw_input(prompt)
			commandline(com)

# =============================
# 
#    Command functions 
#
# =============================

# help file 
def command_help():
	os.system('clear')
	print "Welcome " + uname + "\r"
	print "\r"
	print " ============ Commands List ================\r"
	print " |          help    (commands list)         | \r"
	print " |          private (private messages)      | \r"
 	print " |          members (members list by alias) | \r"
	print " |          online  (online users)          |  \r" 
	print " |          message (message board) 	    | \r"
	print " |          live    (live chat)             | \r"
	print " |          exit    (exit program)          | \r" 
	print " |==========================================| \r"
	print " \r"
	print "\r"
	# drop back to commandline
	com = raw_input("please enter your command > ")
	commandline(com)

# log user out
def log_user_out():
	f = open('/var/tmp/uid.txt','r')
	uid = f.read()
	mydata=[('uid', uid)]
	mydata=urllib.urlencode(mydata)
	path='http://www.example.com/offline.php'
        req=urllib2.Request(path, mydata)
        req.add_header("Content-type", "application/x-www-form-urlencoded")
        response=urllib2.urlopen(req).read()

# members directory 
def members_directory():
	os.system('clear')
	print "Welcome " + uname + "\r"
	action = "online"
	mydata=[('action', action)]
	mydata=urllib.urlencode(mydata)
	path='http://www.example.com/directory.php'
        req=urllib2.Request(path, mydata)
        req.add_header("Content-type", "application/x-www-form-urlencoded")
        response=urllib2.urlopen(req).read()
	print " ========== Members Directory ==========="
	print "    \r "
        print "\r" + response + "\r"
	print "\r"
	com = raw_input("please enter your command > ")
	if (com == "back"):
		os.system('clear')
		programstart(uname)
	commandlist(com)
	

# private messages     
def private_messages():
	os.system('clear')
	print "Welcome " + uname + "\r"
	print "\r"
	print " ============ PM Commands List ================\r"
	print " |          help    (commands list)            | \r"
	print " |          inbox   (messages)                 | \r"
	print " |          write   (write message)            |  \r"  
        print " |          back    (back to index)            |  \r"  
	print " |=============================================| \r"
	print " \r"
        print "\r"
	com = raw_input("please enter your command > ")
	private_message_cmds(com)

# pm cmdline 
def pm_cmdline(com):
	private_message_cmds(com)	

# private message commands 
def private_message_cmds(com):
	#commands array 
	com_array = ['help', 'inbox','write','sent','back']

        # search the array for requested command 
        search = com in com_array
        
        # can't find command warn user and drop them to command line
	if (search == False):
		print "\r"
		com = raw_input("command not found, please try again > ")
		pm_cmdline(com)
	else:
		# command was found now let them run it 
		
		# inbox 
 		if (com == "inbox"):
			pm_inbox(uname)

		# compose new message
		if (com == "write"):
			pm_write_msg()

 		# sent items
		if (com == "sent"):
			show_sent_items()

                # go back 
		if (com == "back"):
			command_help()

# pm inbox
def pm_inbox(uname):
	os.system('clear')
	print "Welcome " + uname + "\r"
	print "\r"
	print " ======== Inbox ========= \r" 
	print "\r"
	print " ID# |  From  | Subject | \n"
	mydata=[('user', uname)]
	mydata=urllib.urlencode(mydata)
	path='http://www.example.com/inbox.php'
        req=urllib2.Request(path, mydata)
        req.add_header("Content-type", "application/x-www-form-urlencoded")
        response=urllib2.urlopen(req).read()
	print "" + response + "\r"
	print " ======================== \r"
	print "\r"
	print "Enter id # to read message or type back to go back"
	com = raw_input(prompt)
        if (com == "back"):
		private_messages()
        if com:
		read_private_msg(com)
        if not com:
	        com = raw_input()
		read_private_msg(com)

# show the sent items 
def show_sent_items():
	os.system('clear')
	print "Welcome " + uname + "\r"
	print "\r"
	print " ======== Sent Items ========= \r"
	print "\r"
	print " ID# |  From  | Subject | \n"
	mydata=[('user', uname)]
	mydata=urllib.urlencode(mydata)
	path='http://www.example.com/sent_items.php'
        req=urllib2.Request(path, mydata)
        req.add_header("Content-type", "application/x-www-form-urlencoded")
        response=urllib2.urlopen(req).read()
	print "" + response + "\r"
	print " ======================== \r"
	print "\r"
	cool = raw_input("enter message id to view it or type delete to delete")
	
# read private message 
def read_private_msg(com):
	os.system('clear')
	mid = com
	mydata=[('msgid',mid), ('uid', uname)]
	mydata=urllib.urlencode(mydata)
	path='http://www.example.com/read.php'
        req=urllib2.Request(path, mydata)
        req.add_header("Content-type", "application/x-www-form-urlencoded")
        response=urllib2.urlopen(req).read()
	if (response == "invalid"):
		print "invalid message id #, please try again"
		time.sleep(2)
		pm_inbox(uname)
	if not response:
		print "\r"
		print "\r"
		print "you have no mesages ID # " + com
		time.sleep(2)
		pm_inbox(uname)
	if (response == "nao"):
		print "\r"
		print "\r"
		print "you have no mesages ID # " + com
		time.sleep(2)
		pm_inbox(uname)
	print "Welcome " + uname + "\r"
	print "\r"
	print "====== Message ID #" + com + " ========\r"
	print "\r"
	print  "\r" + response + "\r"
	print "\r"
	command = raw_input("delete, reply or back? > ")
        
   	if (command == "delete"):
		print "\r"
		print "are you sure you want to delete the messsage? (yes or no)"
		confirm = raw_input(prompt)
		if (confirm == "yes"):
			delete_message(mid)

		if (confirm == "no"):
			print "reply or type back to go back"
			command = raw_input(prompt)
			if (command == "reply"):
				reply_to_message(com)
			if (command == "back"):
				private_messages()
	# reply to Mesasge
	if (command == "reply"):
		reply_to_message(com)
	# go back 
	if (command == "back"):
		private_messages()

# Write a private message
def pm_write_msg():
	os.system('clear')
	print "Welcome " + uname + "\r"
	print "\r"
	print " ===== Compose a mesasge ======"
	print "\r"
	to = raw_input("please enter members alias > ")
	if not to:
		to = raw_input(prompt)
	print "\r"
	subject = raw_input("please enter your subject line > ")
	os.system('clear')
	print "Welcome " + uname + "\r"
	print "\r"
	print " ===== Compose a mesasge ======"
	print "\r"
	print "To: " + to + "\r" 
	print "Subject: " + subject + "\r"
	print "\r"
	print "please enter your message,  type /f  on a new line and enter when finished"
	print "\r"
	text = ""
	stopword = "/f"
	while True:
    		line = raw_input()
    		if line.strip() == stopword:
        		break
    		text += "\n" + line
	os.system('clear')
	print "Welcome " + uname + "\r"
	print "\r"
	print " ===== Compose a mesasge ======"
	print "\r"
	print "To: " + to + "\r" 
	print "Subject: " + subject + "\r"
	print "\r"
 	print "Message: \r"
	print text
        print "\r"
	print "\r"
	answer = raw_input("would you like to send or discard? > ");
        # if users chooses to discard take them back to PM menu
	if (answer == "discard"):
		private_messages()
	if (answer == "send"):
		mydata=[('from', uname), ('to', to), ('subject', subject), ('message', text)]
		mydata=urllib.urlencode(mydata)
		path='http://www.example.com/write.php'
        	req=urllib2.Request(path, mydata)
        	req.add_header("Content-type", "application/x-www-form-urlencoded")
        	response=urllib2.urlopen(req).read()
		if(response == "success"):
			print "your message was sent"
			time.sleep(2)
			private_messages()
	        if(response != "success"):
			print "there was a problem sending your message"
			time.sleep(2)
			private_messages()
		
	
	
# reply to message function
def reply_to_message(com):
	print "please enter your message,  type /f  on a new line and hit enter when finished"
	print "\r"
	text = ""
	stopword = "/f"
	while True:
    		line = raw_input()
    		if line.strip() == stopword:
        		break
    		text += "\n" + line
	mydata=[('msgid',com), ('uname', uname), ('message', text)]
	mydata=urllib.urlencode(mydata)
	path='http://www.example.com/reply.php'
        req=urllib2.Request(path, mydata)
        req.add_header("Content-type", "application/x-www-form-urlencoded")
        response=urllib2.urlopen(req).read()
	print response
	time.sleep(3)
	pm_inbox(uname)

# delete message function 
def delete_message(com):
	mid = com
	mydata=[('msgid', mid), ('uid', uname)]
	mydata=urllib.urlencode(mydata)
	path='http://www.example.com/delete.php'
        req=urllib2.Request(path, mydata)
        req.add_header("Content-type", "application/x-www-form-urlencoded")
        response=urllib2.urlopen(req).read()
	print response
	time.sleep(2)
	pm_inbox(uname)

# ====== begining of encryption ===================
def encrypt(key, msg):
    encryped = []
    for i, c in enumerate(msg):
        key_c = ord(key[i % len(key)])
        msg_c = ord(c)
        encryped.append(chr((msg_c + key_c) % 127))
    return ''.join(encryped)

def decrypt(key, encryped):
    msg = []
    for i, c in enumerate(encryped):
        key_c = ord(key[i % len(key)])
        enc_c = ord(c)
        msg.append(chr((enc_c - key_c) % 127))
    return ''.join(msg)

#==== end of encryption ==========================

# display online users 
def online_users():
	os.system('clear')
	print "Welcome " + uname + "\r"
	action = "online"
	mydata=[('action', action)]
	mydata=urllib.urlencode(mydata)
	path='http://www.example.com/online.php'
        req=urllib2.Request(path, mydata)
        req.add_header("Content-type", "application/x-www-form-urlencoded")
        response=urllib2.urlopen(req).read()
	print "\r"
	print " ========== Online Users ==========="
	print "    \r "
        print "\r" + response + "\r"
	print "\r"
	com = raw_input("please enter your command > ")
	if (com =="back"):
		os.system('clear')
	 	programstart(uname)
	commandline(com)                            

# exit program command 
def command_exit():
	log_user_out()
	print "Good bye, logging you out\r"
	time.sleep(2)
	os.system('clear')
	sys.exit(0)

# chat clinet	
def chat_client():
    # mark user as online in chat
    mydata=[('username', uname)]
    mydata=urllib.urlencode(mydata)
    path='http://www.example.com/onlinechat.php'
    req=urllib2.Request(path, mydata)
    req.add_header("Content-type", "application/x-www-form-urlencoded")
    response=urllib2.urlopen(req).read()
    time.sleep(1)
    os.system('clear')
    print " ===== chatroom users ===== \n"
    print "\r"
    print response
    print "\r"
    print " ============================== \n"				
    host = '98.234.50.89'
    port = '9009'
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
	port = int(port)
        s.connect((host, port))
    except socket.error as e:
        print e
        sys.exit()
     
    print 'Connected to Chat Room. You can start sending messages \n'
    s.send(uname +' has joined the room \n')
    sys.stdout.write('[Me] '); sys.stdout.flush()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        ready_to_read,ready_to_write,in_error = select.select(socket_list , [], [])
         
        for sock in ready_to_read:             
            if sock == s:
                # incoming message from remote server, s
                data = sock.recv(4096)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
                    sys.stdout.write('[Me] '); sys.stdout.flush()     
            
            else :
                # user entered a message
                msg = sys.stdin.readline()
		if (msg == "quit"):
			exit();
		s.send(uname + ': ' + msg)
                sys.stdout.write('[Me] '); sys.stdout.flush() 
              
		
if __name__ == "__main__":
	try:
        	checkuid(ufile)
    	except KeyboardInterrupt:
        	print 'Interrupted'
        sys.exit(0)
	
	
