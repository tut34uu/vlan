from netmiko import ConnectHandler

# Device connection details
device = {
    'device_type': 'cisco_ios',
    'host': '10.10.1.1',
    'username': 'admin',
    'password': 'password',
    'secret': 'enable_password'
}

# New VLAN details
new_vlan_id = 30
new_vlan_name = "VLAN30"

try:
    # Establish connection to the device
    connection = ConnectHandler(**device)
    connection.enable()  # Enter enable mode
    
    # Send configuration command to add new VLAN
    connection.send_config_set([f'vlan {new_vlan_id}', f'name {new_vlan_name}'])
    print(f"VLAN {new_vlan_id} added and named {new_vlan_name}.")
    
    # Disconnect from the device
    connection.disconnect()
    
except Exception as e:
    # Print any errors that occur
    print(f"Error: {e}")
