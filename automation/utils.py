import getpass
from re import search
from pyVim.connect import SmartConnect
import ssl
from pyVim import connect
from pyVmomi import vim

# Get password from user to log into vSphere
passw = getpass.getpass()
username = "nicholas-adm"
s = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
s.verify_mode=ssl.CERT_NONE
si = SmartConnect(host="vcenter.nicholas.local", user=username, pwd=passw, sslContext=s)
aboutInfo=si.content.about
print(aboutInfo.fullName,username)

content = si.RetrieveContent()
virtual_machines = content.viewManager.CreateContainerView(
    content.rootFolder, [vim.VirtualMachine], True)
nameandip1 = {}
nameandip2 = {}
for virtual_machine in virtual_machines.view:
    name = virtual_machine.name
    vmip = virtual_machine.guest.ipAddress
    nameandip1[name] = name
    nameandip2[name] = vmip
    #print(nameandip1)
    #print(virtual_machines.view)
searchfor = input("Search for: ")
#print (nameandip[name])
if searchfor in nameandip1:
    print (nameandip1[searchfor], nameandip2[searchfor])
else:
    print ("Not in dictionary")
    print (nameandip)