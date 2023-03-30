import csv
import os
from jinja2 import Template



source_file = "source.csv"    
template_file = "template.j2" 

# Check if the directory exists, if not create it
if not os.path.exists("generated_configs"):
    os.makedirs("generated_configs")

# Check if the file exists, if not create it
if not os.path.exists(os.path.join("generated_configs", "output.txt")):
    open(os.path.join("generated_configs", "output.txt"), "w").close()

#open the template_file and assign to variable f
with open (template_file) as f: 
    #reading jinja2 environment and assigning to var interface template
    interface_template = Template(f.read(), keep_trailing_newline=True) 
    

with open(source_file) as f:
    reader = csv.DictReader(f)
    for row in reader:
        device_data = interface_template.render(
            hostname =row['hostname'],
            vlan_number = row['vlan_number'],
            name = row['name '],
            ip = row['ip'],
            subnet = row['subnet'],
            group = row['group'],
            virtual_ip = row['virtual_ip'],
            priority = row['priority_num'],
            ip_helper_1 = row['ip_helper_1'],
            ip_helper_2 = row['ip_helper_2'],
            ip_helper_3 = row['ip_helper_3'])
        
        
        with open(os.path.join('generated_configs', 'output.txt'), "a") as f:
            f.write(device_data)