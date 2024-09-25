from netmiko import ConnectHandler

device = {
    'device_type': 'cisco_ios',
    'host': '10.10.1.1',
    'username': 'admin',
    'password': 'password',
    'secret': 'enable_password',  # Optional if the device uses an enable password
    'port': 22  # Default SSH port
}

try:
    print(f"Connecting to {device['host']}...")
    connection = ConnectHandler(**device)
    connection.enable()  # Enter enable mode
    print("Connection successful!")

    # Collecting data
    output = connection.send_command('show version')
    print(output)

    # Save output to a file
    with open('switch_inventory.txt', 'w') as f:
        f.write(output)

    connection.disconnect()
    print("Connection closed.")

except Exception as e:
    print(f"Failed to connect to {device['host']}: {e}")
