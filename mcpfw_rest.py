#
# Python client wrapper for MCP Firmware Rest API
#
import json
import requests

class api(object):
	"""Provides helper functions for accessing the MCP Firmware Rest API.
	"""

	def __init__(self, hostname, port):
		self.hostname = hostname
		self.port = port
		self.baseUrl = 'http://{0}:{1}/mcpfirmware/'.format( hostname, port )
		return super().__init__()

	def root(self):
		"""Determines if the API is accessible and supports a valid API version.
		"""
		#print( 'Contacting system ' + host_name + ' at ' + baseUrl )
		base_resp = requests.get( self.baseUrl ).json()
		#print( json.dumps( base_resp, indent=4 ) )
		if base_resp['ApiVersion'] != 1 :
			raise AppError( 'System does not support the proper API version.' )
		return base_resp

	def state(self):
		"""Returns the current MCP state as a dict
		"""
		stateUrl = self.baseUrl + 'state'
		state_resp = requests.get( stateUrl ).json()
		#print( json.dumps( state_resp, indent=4 ) )
		return state_resp

	def mcpcommand(self, command):
		"""Invokes the specified MCP command.
		"""

		stateUrl = self.baseUrl + 'state'

		command_req = {"Command":command}
		command_resp = requests.post( stateUrl, json=command_req )
		if command_resp.status_code == 202:
			print( '{0} command accepted.'.format( command ) )
			return True
		else:
			try:
				print('Eric! Error')
				error = command_resp.text
				#error = command_resp.load_resp.json()
				#print( '{0} failed: {1}'.format( mcp_command, error['Reason'] ) )
				raise AppError( error['Reason'] )
			except Exception:
				print("Error: ", error)
				#load_resp.raise_for_status()

	def get_mcpcommand(self, command):

		stateUrl = self.baseUrl + command
		print("Eric")
		command_req = {"Command":command}
		command_resp = requests.get(stateUrl).json()#, json=command_req)
		print(command_resp)
		"""
		print("test")
		if command_resp.status_code == 202:
			print('{0} command accepted.'.format(command))
			return True
		else:
			try:
				print("failed")
				error = command_resp.text
				print("Error:", error)
			except Exception:
				print("Error: ", error)
		"""
