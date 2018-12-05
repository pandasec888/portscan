#!/usr/bin/python
# -*- coding: UTF-8 -*-
 
import socket
import optparse
import re
import threading
import sys
print('◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇')
print('◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇')
print('◇◇◇########◇◇◇◇◇◇◇◇◇◇◇##◇◇◇◇◇◇◇◇####◇◇◇###◇◇◇◇◇◇######◇◇◇◇◇◇◇◇◇◇◇◇##◇◇◇◇◇◇◇')
print('◇◇◇◇◇##◇◇##◇◇◇◇◇◇◇◇◇◇###◇◇◇◇◇◇◇◇◇◇###◇◇◇#◇◇◇◇◇◇◇◇◇#◇◇###◇◇◇◇◇◇◇◇◇◇###◇◇◇◇◇◇')
print('◇◇◇◇◇#◇◇◇###◇◇◇◇◇◇◇◇◇###◇◇◇◇◇◇◇◇◇◇###◇◇◇#◇◇◇◇◇◇◇◇◇#◇◇◇##◇◇◇◇◇◇◇◇◇◇###◇◇◇◇◇◇')
print('◇◇◇◇◇#◇◇◇###◇◇◇◇◇◇◇◇◇#◇##◇◇◇◇◇◇◇◇◇#◇##◇◇#◇◇◇◇◇◇◇◇◇#◇◇◇##◇◇◇◇◇◇◇◇◇◇#◇##◇◇◇◇◇')
print('◇◇◇◇◇######◇◇◇◇◇◇◇◇◇##◇##◇◇◇◇◇◇◇◇◇#◇###◇#◇◇◇◇◇◇◇◇◇#◇◇◇###◇◇◇◇◇◇◇◇##◇##◇◇◇◇◇')
print('◇◇◇◇◇#◇◇◇◇◇◇◇◇◇◇◇◇◇◇######◇◇◇◇◇◇◇◇#◇◇####◇◇◇◇◇◇◇◇◇#◇◇◇##◇◇◇◇◇◇◇◇◇######◇◇◇◇')
print('◇◇◇◇◇#◇◇◇◇◇◇◇◇◇◇◇◇◇##◇◇◇##◇◇◇◇◇◇◇◇#◇◇◇###◇◇◇◇◇◇◇◇◇#◇◇◇##◇◇◇◇◇◇◇◇##◇◇◇##◇◇◇◇')
print('◇◇◇◇◇#◇◇◇◇◇◇◇◇◇◇◇◇◇##◇◇◇##◇◇◇◇◇◇◇◇3◇◇◇◇##◇◇◇◇◇◇◇◇◇#◇◇###◇◇◇◇◇◇◇◇##◇◇◇##◇◇◇◇')
print('◇◇◇#####◇◇◇◇◇◇◇◇◇◇###◇◇#####◇◇◇◇◇####◇◇◇#◇◇◇◇◇◇◇#######◇◇◇◇◇◇◇◇###◇◇#####◇◇')
print('◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇')
print('◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇')
print('◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇')
print('◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇◇')

def anlyze_host(targe_host):
	try:
		pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
		match = pattern.match(targe_host)
		if match:
			return(match.group())
		else:
			try:
			
				targe_host = socket.gethostbyname(target_host)
				return(target_host)
			except Exception as err:
				print('地址解析错误:',err)
				exit(0)
	except Exception as err:
		print('错误1:',sys.exc_info()[0],err)
		print(parser.usage)
		exit(0)

def anlyze_port(target_port):
    try:
        pattern = re.compile(r'(\d+)-(\d+)')    
        match = pattern.match(target_port)
        if match:
            start_port = int(match.group(1))
            end_port = int(match.group(2))
            return([x for x in range(start_port,end_port + 1)])
        else:
            return([int(x) for x in target_port.split(',')])
    except Exception as err:
        print('错误2:',sys.exc_info()[0],err)
        print(parser.usage)
        exit(0)
		
def scanner(target_host,target_port):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(5)
    try:
        s.connect((target_host,target_port))
        print('[+]%s的%3s端口:打开' % (target_host,target_port))
    except socket.timeout:
        print('[-]%s的%3s端口:关闭' % (target_host,target_port))
    except Exception as err:
        print('端口没有开放:',sys.exc_info()[0],err)
        exit(0)
		
def main():
   usage = 'Usage:%prog -h <host> -p <port>'
   parser = optparse.OptionParser(usage,version='%prog panda1.0')
   parser.add_option('--host',dest='target_host',type='string',
                     help='需要扫描的主机,域名或IP')
   parser.add_option('--port',dest='target_port',type='string',
                    help='扫描的端口，example:1-100 or 80,因为程序有缺陷，建议采用第二种方式扫描')
   (options,args) = parser.parse_args()
   if options.target_host == None or options.target_port == None:
      print(parser.usage)
      exit(0)
   else:
      target_host = options.target_host
      target_port = options.target_port

   target_host = anlyze_host(target_host)
   target_port = anlyze_port(target_port)

   for port in target_port:
      t = threading.Thread(target=scanner,args=(target_host,port))
      t.start()

if __name__ == '__main__':
    main()


