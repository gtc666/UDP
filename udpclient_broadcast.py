#!/usr/bin/env python
# -*- coding:utf8 -*-

import sys
import types
reload(sys)
sys.setdefaultencoding('utf-8')

import socket

class UdpClient(object):
    def tcpclient(self):
        clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        clientSock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        
        addr = '192.168.31.111'
        #addr = 'aaaa::212:4b00:a55:2a04'
        port = 7777
        sendDataLen = clientSock.sendto("Hi", (addr, port))
        recvData = clientSock.recvfrom(1024)
        #print "sendDataLen: ", sendDataLen, type(addr)
        print "recvData: ", recvData[0], recvData[1][0]
        return recvData[1]
        
        clientSock.close()

if __name__ == "__main__":
    udpClient = UdpClient()
    recv = udpClient.tcpclient()
    print "sensor's ip: ", recv[0]
