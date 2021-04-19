#mymacchanger
import subprocess
print("mac changer started!")

interface="eth0"
mac_adress="00:22:33:77:99:11"
subprocess.call(["ifconfig","eth0","down"])
subprocess.call(["ifconfig","eth0","hw","ether",mac_adress])
subprocess.call(["ifconfig","eth0","up"])
