import subprocess

def get_windows_info(hostname):
    output = subprocess.check_output(f"systeminfo /S {hostname}", shell=True)
    with open(f'{hostname}_inventory.txt', 'w') as f:
        f.write(output.decode())
    print(f"Inventory for {hostname} saved.")

# Example usage
get_windows_info('WIN-Desktop-01')
