from create-ticket import * 

devices = []

try: 

   resp = get(api="network-device")
   status = resp.status_code
   response_json = resp.json()
   devices = response_json["response"]

except:

      print("Something went wrong")
      sys.exit()

if status != 200:
   print (resp.text)
   sys.exit()

if devices == []:
   print ("No devices found on current host")
   sys.exit()

list_of_devices = []

i=0
for item in devices:

    i += 1
    list_of_devices.append([i,item["hostname"],item["ipaddress"],item["mac address"]])

print (tabulate(list_of_device,[headers='number','hostname','ip'],tablefmt = "rst"))

def getnetworkdevicescount(self, **nwargs):

    thread = api.getnetworkdevicescount(async=True)
    result = thread.get()
if nwargs.get('async'):
   return self.getnetworkdevicescount(**nwargs)
else:
    (data) self.getnetworkdevicescount(**nwargs)
    return data

getnetworkdevicescount(self,**nwargs)

"""controller='sandboxapic.cisco.com'
#controller='devnetapi.cisco.com/sandbox/apic_em'


# put the ip address or dns of your apic-em controller in this url
url = "https://" + controller + "/api/v1/ticket"

#the username and password to access the APIC-EM Controller
payload = {"username":"devnetuser","password":"Cisco123!"}

#Content type must be included in the header
header = {"content-type": "application/json"}

#Performs a POST on the specified url to get the service ticket
response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)

#convert response to json format
r_json=response.json()

print(r_json)
#parse the json to get the service ticket
ticket = r_json["response"]["serviceTicket"]

# URL for Host REST API call to get list of exisitng hosts on the network.
url = "https://" + controller + "/api/v1/host?limit=1&offset=1"

#Content type must be included in the header as well as the ticket
header = {"content-type": "application/json", "X-Auth-Token":ticket}

# this statement performs a GET on the specified host url
response = requests.get(url, headers=header, verify=False)

# json.dumps serializes the json into a string and allows us to
# print the response in a 'pretty' format with indentation etc.
print ("Hosts = ")
print (json.dumps(response.json(), indent=4, separators=(',', ': ')))

r_resp=response.json()

print(r_resp["response"][0]["hostIp"])"""


