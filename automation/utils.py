from distutils.command.config import config
import getpass
from html.entities import name2codepoint
import imp
from re import search
from pyVim.connect import SmartConnect
import ssl
from pyVim import connect
from pyVmomi import vim
import atexit
from pprint import pprint


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
# name dictionary
vmname = {}
# ip dictionary
ipaddr = {}
# power dictionary
powered = {}
corecount = {}

mem = {}

toPowerOn = input("VM to power on: ")

for virtual_machine in virtual_machines.view:
    name = virtual_machine.name
    if (toPowerOn == name):
        virtual_machine.PowerOff
        print("Power")

    vmip = virtual_machine.guest.ipAddress
    #print (virtual_machine.summary)
    power = "powered off"
    if (vim.VirtualMachinePowerState.poweredOn == virtual_machine.runtime.powerState):
        power = "powered on"
    else:
        power = "powered off"
    #print (virtual_machine.hardware.cpuInfo)
    vmname[name] = name
    ipaddr[name] = vmip
    powered[name] = power
    corecount[name] = virtual_machine.summary.config.numCpu
    mem[name] = virtual_machine.summary.config.memorySizeMB / 1024
    #print (mem)
searchfor = input("Search for: ")
print('{:<32}{:<32}{:<32}{:<32}{:<32}'.format("Name", "IP Address", "Power State", "Core Count", "Memory (GB)"))
print('{:<32}{:<32}{:<32}{:<32}{:<32}'.format("----", "----------", "-----------", "----------", "-----------"))
for key, val in vmname.items():
    if searchfor in key:
        print('{:<32}{:<32}{:<32}{:<32}{:<32}'.format(vmname[key], str(ipaddr[key]), powered[key], corecount[key], mem[key]))
        #print(tabulate([vmname[key], ipaddr[key], powered[key], corecount[key], mem[key]], headers=[key]))


