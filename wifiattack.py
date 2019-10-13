import pywifi
import time
from pywifi import const

def wificonnect(pwd):
    wifi=pywifi.PyWiFi()
    iface=wifi.interfaces()[0]
    wifistate=iface.status()
    iface.disconnect()
    time.sleep(2)
    if wifistate==const.IFACE_CONNECTED:
        print("ok")
    else:
        myprofile=pywifi.Profile()
        #wifi名称
        myprofile.ssid=getssid()
        #网卡开放
        myprofile.auth=const.AUTH_ALG_OPEN
        myprofile.akm.append(const.AKM_TYPE_WPA2PSK)
        myprofile.cipher=const.CIPHER_TYPE_CCMP
        myprofile.key=pwd
        #去除所有连接
        iface.remove_all_network_profiles()
        #新的连接
        tep_profile=iface.add_network_profile(myprofile)
        iface.connect(tep_profile)
        time.sleep(5)
        if iface.status()==const.IFACE_CONNECTED:
            return True
        else:
            return False

def readpass():
    mypwfile=''
    pw=open(mypwfile,'r')
    while True:
        try:
            pwstr=pw.readline()
            bool=wificonnect(pwstr)
            if bool:
                print("密码正确：",pwstr)
                break
            else:
                print('密码错误',pwstr)
        except:
            continue

#readpass()

def getssid():
    wifi=pywifi.PyWiFi()
    iface=wifi.interfaces()[0]
    wifistate=iface.status()
    print(wifistate)
    #扫描
    iface.scan()
    re=iface.scan_results()
    i=0
    for ssd in re:
        print(i,ssd.ssid)
        i=i+1
    #print(re[0].ssid)
    cssd=int(input('选择哪个ssid,输入数字'))
    return re[cssd].ssid
print(getssid())