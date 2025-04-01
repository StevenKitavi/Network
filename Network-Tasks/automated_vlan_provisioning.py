def print_vendor(net_vendor):
    print(net_vendor)

vendors = ['arista', 'juniper', 'cisco', 'big_switch']


for vendor in vendors:
    print_vendor(vendor)


#Create two functions to help automate VLAN provisioning

#First function get_commands() obtains the required commands to send to a network device. A
# Accepts two parameters : VLAN ID
# using the parameter vlan and VLAN NAME using the parameter name


#Second function push_commands() pushes the actual commands that are gathered from get_commands() to a given list of devices
# The function also accepts two paramters: device which is the device to send the commands to and commands - the list of the commands to send.

#the push will not happen in the function but rather it will print the commands on the terminal to stimulate command execution.




def get_commands(vlan, name):
    commands = []
    commands.append('vlan ' + vlan)
    commands.append('name ' + name)



    return commands


def push_commands(device, commands):
    print('Connecting to: ' + device)
    for cmd in commands:
        print('Sending command:  ' + cmd)


devices = ['switch1', 'switch2', 'switch3']


vlans = [{'id': '10', 'name': 'USERS'}, {'id': '20', 'name': 'VOICE'}, {'id': '30', 'name': 'WLAN'}]



for vlan in vlans:
    id = vlan.get('id')
    name = vlan.get('name')
    print('\n')
    print('CONFIGURING VLAN:' + id)
    commands = get_commands(id, name)
    for device in devices:
        push_commands(device, commands)
        print('\n')

