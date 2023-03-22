from netmiko import ConnectHandler
# set un equal to your username
# set pw equal to your password
un = "admin"
pw = "cisco123!"
ios_type = "cisco_ios_telnet"
ip_addr = "192.168.128.23"
port = "5003"


net_connect = ConnectHandler(device_type=ios_type, ip=ip_addr, port=port, username=un, password=pw)
output = net_connect.find_prompt()

# 'LAB'>’ – Returns the current prompt as Unicode string
print(output)
net_connect.disconnect()
exit()
