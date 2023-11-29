import optparse # for input
import subprocess # for kali linux terninal command

def get_user_input():
    object = optparse.OptionParser()
    object.add_option("-i","--interface",dest="interface",help="interface to chnage!") #interface--> eth0 or wlan0
    object.add_option("-m", "--mac",dest="mac_address",help="mew mac address") #MAC

    return object.parse_args()

def mac_change (user_interface,user_mac_address):
    subprocess.call(["ifconfig",user_interface,"down"])
    subprocess.call(["ifconfig",user_interface,"hw","ether",user_mac_address])
    subprocess.call(["ifconfig",user_interface,"up"])

def new_mac(interface):
    ifconfig = subprocess.check_output(["ifconfig",interface])
    print(ifconfig)

print("MAC cahnger started!")
(user_input,arguments) = get_user_input() #for get_user_input method work with other method
mac_change(user_input.interface,user_input.mac_address) #link get_user_input with mac_change for working 
new_mac(user_input.interface) # if we start get_user_input, new_mac is started as 3th


#(Kali) LINUX Terminal: python isa.py -i||--interface eth0||wlan0 -m||--mac **00:11:11:22:22:22**
