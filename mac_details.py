import requests 
import argparse
import time
from mac import mac
  
print("[*] Welcome") 
  
# # Function to get the interface name 
# def get_arguments(): 
    
#     # This will give user a neat CLI 
#     parser = argparse.ArgumentParser() 
      
#     # We need the MAC address 
#     parser.add_argument("-m", "--macaddress", 
#                         dest="mac_address", 
#                         help="MAC Address of the device. "
#                         ) 
#     options = parser.parse_args() 
      
#     # Check if address was given 
#     if options.mac_address: 
#         return options.mac_address 
#     else: 
#         parser.error("[!] Invalid Syntax. "
#                      "Use --help for more details.") 


def get_mac_details(mac_address): 
      
    # We will use an API to get the vendor details 
    url = "https://api.macvendors.com/"
      
    # Use get method to fetch details 
    response = requests.get(url+mac_address)
    # if response.status_code != 200: 
    #     raise Exception("[!] Invalid MAC Address!") 
    return response.content.decode() 
  
# Driver Code 
def main(dummy_mac=[]):
        macs = mac()
        if dummy_mac != []:
          macs = dummy_mac

        # print("IP                  MAC                       Vendor Name")
        for k in macs.keys():
            try:
                mac_address = macs[k]
                # print("[+] Checking Details...") 
                vendor_name = get_mac_details(mac_address) 
                print(f"{k}         {mac_address}         {vendor_name}")
            except:
                print('Something went wrong')
            time.sleep(2)

main()
