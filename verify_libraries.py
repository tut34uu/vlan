import pkg_resources

# List of essential libraries for VLAN automation
required_libraries = {'netmiko', 'datetime'}

# Get installed libraries
installed_libraries = {pkg.key for pkg in pkg_resources.working_set}

# Verify if all required libraries are installed
missing_libraries = required_libraries - installed_libraries
if not missing_libraries:
    print("All required libraries are installed.")
else:
    print(f"Missing libraries: {missing_libraries}")
