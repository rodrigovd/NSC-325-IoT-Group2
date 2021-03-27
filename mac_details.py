import requests 
import argparse
import time
import pandas as pd
import numpy as np
from mac import mac
from tabulate import tabulate

url = 'http://standards-oui.ieee.org/oui/oui.csv'
  
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

def get_vendor_details(url='http://standards-oui.ieee.org/oui/oui.csv'):
    df=pd.read_csv(url,dtype=str)
    return df
    
def main_mac(Demo=True, dummy= {}
            ): 
    if Demo:
        macs= dummy
    else:
        macs = mac()
    dic = {}
    ip_list = []
    m_list = []
    vendor_list = []
    loc_list = []
    df = get_vendor_details()
    for ip,m in zip(macs.keys(), macs.values()):
        mac_ids =m[:8]
        nes = mac_ids.replace(':','')
        search = f'{nes.upper()}'
    #     print(search)
        ip_list.append(ip)
        m_list.append(m)
        ans = df[df.Assignment == search]
        vendor = str(ans['Organization Name'])[6:-40].lstrip()
        l = str(ans['Organization Address'])[6:].strip()
        loc =l.replace(' \nName: Organization Address, dtype: object','')
#         print(vendor)
        if '([],' in vendor:
            vendor_list.append('Not Discovered')
            loc_list.append('Not Discovered')

    #     n.append(ans['Organization Name'])
        else:
            vendor_list.append(vendor)
            loc_list.append(loc)
    dic['ip'] = ip_list
    dic['mac adresses'] = m_list
    dic['vendor'] = vendor_list
    dic['location'] = loc_list
    df2 = pd.DataFrame(dic)
    print(df2)

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
