# -*- coding: UTF-8 -*-
#!/usr/bin/env python
import sys,socket

'''
Usage : 
    ->   python dnsburp.py baidu.com
    ->   python dnsburp.py baidu.com > 1.log
'''
socket.setdefaulttimeout(2)

class HOST():
    def __init__(self,host):
        self.host = host
        self.SLD_LIST = []
        self.process_SLD()
        self.for_SLD()
    
    def process_SLD(self):
        '''
        从 host.txt 读取二级域名，批量加入 SLD_LIST
        '''
        try:
            f = open("hosts.txt", "r")
            line = f.readlines()
            for SLD in line:
                self.SLD_LIST.append(SLD.rstrip('\n')+"."+ self.host)
        except:
            print "Read File Error"
        finally:
            f.close()
    def query_dns(self,SLD_HOST):
        '''
        查询DNS函数
        '''
        try:
            ip = socket.getaddrinfo(SLD_HOST,None)
            if ip:
                sys.stdout.write(SLD_HOST + " ")
                for _ip in ip:
                    sys.stdout.write(str(_ip[4][0]+" "))
                print ""
        except:
            pass      
            
    def for_SLD(self):
       '''
       写一个for 循环查询 SLD_LIST 里边的域名
       '''
       for SLD_HOST in self.SLD_LIST:
           self.query_dns(SLD_HOST)

if __name__ == "__main__":
    try:
        obj = HOST(sys.argv[1])
    except IndexError:
        filename = sys.argv[0]
        print "  Usage: python %s <host> \n  Example: python  %s baidu.com " % (filename,filename)

