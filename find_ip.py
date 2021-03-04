import netifaces
def find_gateway():
      Interfaces= netifaces.interfaces()
      for inter in Interfaces:
           if inter == "enp2s0":
                temp_list = []
                Addresses = netifaces.ifaddresses(inter)
                gws = netifaces.gateways()
                temp_list = list (gws['default'][netifaces.AF_INET])
                count =0 
                for item in temp_list:
                      count +=1
                      if count ==1:
                           # print (item)
                           return item
                      else:
                           pass
find_gateway()
