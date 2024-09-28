from netmiko import ConnectHandler

# Switch details
device = {
    'device_type': 'cisco_ios',
    'host': '10.10.1.1',  # Example IP address
    'username': 'admin',
    'password': 'password',
    'secret': 'enable_password',  # Optional
    'port': 22  # Default SSH port
}

try:
    print(f"Connecting to {device['host']}...")
    connection = ConnectHandler(**device)
    connection.enable()  # Enter enable mode
    print("Connection successful!")

    # Collecting switch data (inventory)
    output = connection.send_command('show version')
    print(output)

    # Save inventory to a file
    with open('switch_inventory.txt', 'w') as f:
        f.write(output)

    connection.disconnect()
    print("Connection closed. Inventory saved to switch_inventory.txt")

except Exception as e:
    print(f"Failed to connect to {device['host']}: {e}")
