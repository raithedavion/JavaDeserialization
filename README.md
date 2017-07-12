# JavaDeserialization


Websphere.py is based on original work by Fox Glove Security.

Description:

The script takes what Steve Breen did in the foxglove blog and puts it in a python script. Using the foxglove sample POST request, I made this pythons cript that behaves much like the weblogic.py script they have on their github. 

Usage:

python websphere.py protocol targetip port pathtoysoserial 'command'



Sources: 
Foxglove blog: https://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability/
Foxglove github: https://github.com/foxglovesec/JavaUnserializeExploits
ysoserial: https://github.com/frohoff/ysoserial/


rmi.py is based on the premise of WebSphere.py.

Description:

The script replaces the use of ysoerial with static code.  It has been tested on opennms and vmware vdp.  

Usage:

python rmi.py targetip port usessl 'command'
