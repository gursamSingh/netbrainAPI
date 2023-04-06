import requests
import json

# Set the server URL and API endpoint
server_url = "http://your_netbrain_server/ServicesAPI/"
endpoint_url = server_url + "API/CMDB/device/getGroupDevices"

# Set the request headers and parameters
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "Token": "your_api_token"
}
params = {
    "groupName": "your_device_group_name"
}

# Send the HTTP GET request
response = requests.get(endpoint_url, headers=headers, params=params)

# Parse the JSON response
if response.status_code == 200:
    data = json.loads(response.content.decode('utf-8'))
    # Access the device group data in the 'data' dictionary
else:
    print("Failed to retrieve device group:", response.status_code, response.text)
