from scapy.all import ARP, Ether, srp
from find_ip import find_gateway


def mac():
	mac_dict = {}

	# target_ip = "192.168.0.1/24"
	target_ip = str(find_gateway()) + "/24"
	# IP Address for the destination
	# create ARP packet
	arp = ARP(pdst=target_ip)
	# create the Ether broadcast packet
	# ff:ff:ff:ff:ff:ff MAC address indicates broadcasting
	ether = Ether(dst="ff:ff:ff:ff:ff:ff")
	# stack them
	packet = ether/arp

	result = srp(packet, timeout=3, verbose=0)[0]

	# a list of clients, we will fill this in the upcoming loop
	clients = []

	for sent, received in result:
	    # for each response, append ip and mac address to `clients` list
	    clients.append({'ip': received.psrc, 'mac': received.hwsrc})

	# print(clients)
	# print("Available devices in the network:")
	# print("IP" + " "*18+"MAC")
	for client in clients:
	    mac_dict[client['ip']] = client['mac']
	    # print("{:16}    {}".format(client['ip'], client['mac']))

	    if (client['mac'] == "f4:f5:e8:37:67:92"):  #Testing mac address filter
	        print("Success")
	return mac_dict

