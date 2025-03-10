'''
This is the main program. 
It reads packaging.txt, processes packaging data, and saves results in JSON.
'''

import json
from packaging import parse_packaging, calc_total_units, get_unit

packages = []

try:
    with open('data/packaging.txt', "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            
            package = parse_packaging(line)  
            total_units = calc_total_units(package) 
            unit = get_unit(package) 
            
            print(f"{line} => total units: {total_units} {unit}") 
            packages.append(package) 

    with open('data/packaging.json', "w") as json_file:
        json.dump(packages, json_file, indent=4)

    print("\nPackaging data saved to data/packaging.json")

except FileNotFoundError:
    print("Error: data/packaging.txt not found!")
except Exception as e:
    print(f"Unexpected error: {e}")
