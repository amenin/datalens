### DATA FORMATTING V3

import json

# # Load the JSON file
# with open('results/v3/visu/sim_links_tasks.json', 'r') as f:
#     data = json.load(f)

# # Create a list to store the modified entries
# modified_entries = []

# # Iterate through the original entries
# for entry in data:
#     p_values = entry['p']['value'].split(', ')

#     for p_value in p_values:
#         # Create a new entry with the split "p" value
#         new_entry = {
#             "p": {
#                 "value": p_value
#             },
#             "s": {
#                 "value": entry['s']['value']
#             },
#             "o": {
#                 "value": p_value
#             },
#             "label": {
#                 "value": entry['s']['value']
#             },
#             "authorList": entry["authorList"],
#             "style1": {
#                 "value":"db" 
#             },
#             "style2": {
#                 "value":"task" ########
#             }
#         }

#         modified_entries.append(new_entry)

# # Write the modified entries to a new JSON file
# with open('results/v3/visu/full_task.json', 'w') as f:
#     json.dump(modified_entries, f, indent=2)


### DATA FORMATTING V4

# # Load the JSON file
# with open('results/v3/full_cat.json', 'r') as f:
#     data = json.load(f)

# # Create a list to store the modified entries
# modified_entries = []

# # Iterate through the original entries
# for entry in data:
#     p_values = entry['p']['value'].split(', ')

#     for p_value in p_values:
#         # Create a new entry with the split "p" value
#         new_entry = {
#             "p": {
#                 "value": p_value
#             },
#             "s": {
#                 "value": entry['s']['value']
#             },
#             "o": {
#                 "value": entry['o']['value']
#             },
#             "label": {
#                 "value": p_value
#             }
#         }

#         modified_entries.append(new_entry)

# # Write the modified entries to a new JSON file
# with open('results/v3.2/full_task.json', 'w') as f:
#     json.dump(modified_entries, f, indent=2)

### DATA FORMATTING V3.2
import re

# Load the JSON file
with open('results/v3/full_task.json', 'r') as f:
    data = json.load(f)

# Create a list to store the modified entries
modified_entries = []

# Define a regular expression pattern to match the URL
pattern = r"URL: (https://\S+)"

# Search for the URL using the pattern

# Iterate through the original entries
for entry in data:
    p_values = entry['p']['value'].split(', ')

    for p_value in p_values:
        # Search for the URL using the pattern
        match = re.search(pattern, entry["authorList"]["value"])
        if match:
            url = match.group(1)
        else:
            url = '#'  # Handle the case where no URL is found
        new_entry = {
            "p": {
                "value": entry['s']['value']
            },
            "s": {
                "value": entry['s']['value']
            },
            "o": {
                "value": p_value
            },
            "label": {
                "value": entry['s']['value']
            },
             "link": {
                "value": url
            },
            "authorList": entry["authorList"],
            "style1": {
                "value":"db" 
            },
            "style2": {
                "value":"task" ########
            }
        }

        modified_entries.append(new_entry)

# Write the modified entries to a new JSON file
with open('results/v3.2/full_task.json', 'w') as f:
    json.dump(modified_entries, f, indent=2)