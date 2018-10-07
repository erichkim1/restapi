
import mcpfw_rest

# Test to see if you can create an emulated disk
def create_EmulatedDisks():
    host_name = 'kime-win2016'
    port_num = 53210
    capacityMB = "135"
    command = 'disks'
    payload = {
        "CapacityMB": capacityMB,
        "DiskFormat":"Native",
        "FileSystemPath":"C:\\Unisys\\MCP\\test000.asd"
        }

    try:
        proxy = mcpfw_rest.api(host_name, port_num)

        mcp_state = proxy.state()
        curr_state = mcp_state['State']
        print('MCP state is {0}; initiating {1}...'.format( curr_state, command))

        rslt = proxy.put_command(command, payload)
        print(rslt)
    except Exception as ex:
        print (type( ex ))
        print (str( ex))

def main():
    print('Test Case #1: Test to see if an emulated disk can be created')
    create_EmulatedDisks()

if __name__ == "__main__":
    main()
