COMMANDS = {
    'description': 'description {}',
    'speed': 'speed {}',
    'duplex': 'duplex {}'
}

print(COMMANDS)
type(COMMANDS)

CONFIG_PARAMS = {
    'description': 'auto description by Python',
    'speed': '10000',
    'duplex': 'auto'

}
print(CONFIG_PARAMS)
type(CONFIG_PARAMS)

commands_list = []
for feature, value in CONFIG_PARAMS.items():
    command = COMMANDS.get(feature).format(value)
    commands_list.append(command)

commands_list.insert(0, 'interface Eth1/1')

print(commands_list)
