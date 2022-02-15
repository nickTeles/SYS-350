import getpass
from pyVim.connect import SmartConnect
import ssl
passw = getpass.getpass()
s = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
s.verify_mode=ssl.CERT_NONE
si = SmartConnect(host="vcenter.nicholas.local", user="nicholas-adm", pws=passw, SSLContext=s)
aboutInfo=si.content.about
print(aboutInfo)
