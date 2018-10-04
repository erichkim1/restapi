#
# Python example of calling the MCP Firmware Rest API to issue an MCP command.
#
import getopt
import sys

import mcpfw_rest

class options(object):
	port_number = 53210
	host_name = ''
	mcp_command = ''

	def __init__(self, argv):
		self.args = argv

	def process_args(self):
		try:
			opts, args = getopt.getopt( self.args[1:], "hc:s:p:" )
		except getopt.GetoptError as err:
			return options.usage( str(err) )

		for o, a in opts:
			if o == '-h':
				return options.usage()
			elif o == '-s':
				self.host_name = a
			elif o == '-p':
				self.port_number = a
			elif o == '-c':
				self.mcp_command = a
			else:
				return options.usage( "Unrecognized option {0}".format( o ) )

		if not self.mcp_command:
			return options.usage( "No command parameter provided." )
		if not self.host_name:
			return options.usage( "No hostname parameter provided." )

		return True

	def usage( error = "" ):
		if error:
			print()
			print( 'ERROR: ' + error )
		print()
		print( 'Issues the specified MCP command to the specified host.' )
		print()
		print( 'USAGE:' )
		print( '    mcp_command.py -c <command> -s <hostname> [-p <port>]' )
		return False


def main():
	opts = options( sys.argv )
	if not opts.process_args():
		sys.exit(2)

	try:
		proxy = mcpfw_rest.api( opts.host_name, opts.port_number )
		api_root = proxy.root()

		mcp_state = proxy.state()
		curr_state = mcp_state['State']
		print( 'MCP state is {0}; initiating {1}...'.format( curr_state, opts.mcp_command ) )

		proxy.mcpcommand( opts.mcp_command )
	except Exception as ex:
		print( type( ex ) )
		print( str( ex )  )

if __name__ == "__main__":
	main()
