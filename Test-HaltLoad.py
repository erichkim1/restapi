
import sys

import mcpfw_rest
import mcp_command
import requests
import json


hostname = "http://kime-win2016"
portNum = '53210'
desiredMemorySize = 77
payload = {'DesiredMcpMemoryMW':str(desiredMemorySize)}
command = 'state'
url = hostname + ":" + portNum + "/mcpfirmware/"+ command

try:
    proxy = mcpfw_rest.api( hostname, portNum)
    api_root = proxy.root()

    mcp_state = proxy.state()

    #mcp_command.options(-c Load -s kime-win2016)
    mcp_command.main()
    #mcp_command.py -c Load -s kime-win2016

except Exception as ex:
    print(type( ex ))
    print( str( ex ))

print('worked!')


cmd_resp = requests.get(url).json()
print(cmd_resp)
