from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '10.10.1.1',
    'username': 'admin',
    'password': 'password',
    'secret': 'enable_password'
}

try:
    connection = ConnectHandler(**device)
    connection.enable()
    vlan_output = connection.send_command('show vlan brief')
    print(vlan_output)
    connection.disconnect()
except Exception as e:
    print(f"Error: {e}")
