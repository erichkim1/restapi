#
# Python example of calling the MCP Firmware Rest API to get basic status information.
#
import getopt
import sys

import mcpfw_rest

class options(object):
	port_number = 53210
	host_name = ''

	def __init__(self, argv):
		self.args = argv

	def process_args(self):
		try:
			opts, args = getopt.getopt( self.args[1:], "hs:p:" )
		except getopt.GetoptError as err:
			return options.usage( str(err) )

		for o, a in opts:
			if o == '-h':
				return usage()
			elif o == '-s':
				self.host_name = a
			elif o == '-p':
				self.port_number = a
			else:
				return options.usage( "Unrecognized option {0}".format( o ) )

		if self.host_name == '':
			return options.usage( "No hostname parameter provided." )

		return True

	def usage( error = "" ):
		if error:
			print()
			print( 'ERROR: ' + error )
		print()
		print( 'Retrieves basic state information.' )
		print()
		print( 'USAGE:' )
		print( '    mcp_state.py -s <hostname> [-p <port>]' )
		return False


def main():
	opts = options( sys.argv )
	if not opts.process_args():
		sys.exit(2)

	try:
		proxy = mcpfw_rest.api( opts.host_name, opts.port_number )
		api_root = proxy.root()

		print( '{0}  [{1} -- {2}]'.format( api_root['SystemName'], api_root['Series'], api_root['Style'] ) )
		print( '   Version {0}'.format( api_root['SoftwareVersion'] ) )

		mcp_state = proxy.state()
		print( '   MCP: {0}'.format( mcp_state['State'] ) )

	except Exception as ex:
		print( type( ex ) )
		print( str( ex )  )

if __name__ == "__main__":
	main()
