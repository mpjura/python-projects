'''
**Port Scanner** - Enter an IP address and a port range where the program will then attempt to find open ports on the given computer by connecting to each of them. On any successful connections mark the port as open.
'''
import socket
import subprocess
import sys
from datetime import datetime

subprocess.call('clear', shell = True )

remoteServer = raw_input('Enter host to be scanned: ')
remortServerIP = socket.gethostbyname( remoteServer )

print '-' * 50
print 'Please wait, scanning remote host', remortServerIP
print '-' * 50

start = datetime.now()

try:
	for port in range(1,1025):
		sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
		result = sock.connect_ex( (remortServerIP, port) )
		
		if result == 0:
			print 'Port %s:\t Open' % port
		
		sock.close()

except KeyboardInterrupt:
	print 'You press Ctrl-C'
	sys.exit()

except socket.gaierror:
	print 'Hostname could not be resolved.'
	sys.exit()

except socket.error:
	print 'Couldn\'t connect to server.'
	sys.exit()

end = datetime.now()

print 'Scanning complete in: ', end - start