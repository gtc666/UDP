#!/usr/bin/env python
# -*- coding:utf8 -*-

import sys
import types
reload(sys)
sys.setdefaultencoding('utf-8')

import socket

class UdpServer(object):
    def tcpServer(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind(('', 7777))       # 绑定同一个域名下的所有机器
        
        while True:
            revcData, (remoteHost, remotePort) = sock.recvfrom(1024)
            print("[%s:%s] connect" % (remoteHost, remotePort))     # 接收客户端的ip, port
            #sendDataLen = sock.sendto("this is send  data from server", (remoteHost, remotePort))
            print "remoteHost: ", remoteHost
            print "revcData: ", revcData
            
        #print "sendDataLen: ", sendDataLen
        
        sock.close()

if __name__ == "__main__":
    udpServer = UdpServer()
    (name, ip) = udpServer.tcpServer()
