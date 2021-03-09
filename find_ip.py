import netifaces

print("Finding your Interface.....")
list_of_interfaces = netifaces.interfaces()
print(list_of_interfaces)

def interface():
     interf = input("Enter your interface:")
     if interf in list_of_interfaces:
          return interf
     else:
          print("Interface not found be sure to enter your selecction excatly")
          return interface()

def find_gateway():
          inter = interface()
          temp_list = []
          Addresses = netifaces.ifaddresses(inter)
          gws = netifaces.gateways()
          temp_list = list (gws['default'][netifaces.AF_INET])
          count =0 
          for item in temp_list:
               count +=1
               if count ==1:
                    print (item)
                    return item
               else:
                    pass
# find_gateway()
