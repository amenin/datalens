### MATCHING SIMILARITY

import json
import os
from collections import defaultdict
from itertools import combinations

# # Function to compute Jaccard similarity
# def jaccard_similarity(tags1, tags2):
#     set1 = set(tags1)
#     set2 = set(tags2)
#     intersection = set1.intersection(set2)
#     union = set1.union(set2)
#     if not union:  # Avoid division by zero
#         return 0
#     return len(intersection) / len(union)

### MATCHING SIMILARITY

# Function to find matching tags between two entries
def find_matching_tags(tags1, tags2):
    set1 = set(tags1)
    set2 = set(tags2)
    common_tags = set1.intersection(set2)
    return common_tags

# Function to extract task_categories from tags
def extract_values(entry, key):
    values = []
    if 'tags' in entry and isinstance(entry['tags'], list):
        for tag in entry['tags']:
            if tag.startswith(f"{key}:"):
                values.append(tag.split(f"{key}:")[1])
    return values


def extractTaskDict(data):
    tasks_dict = {}
    for item in data:
        tasks = extract_values(item, 'task_categories')  # Assuming extract_task_categories returns a list of tasks
        for task in tasks:
            if task in tasks_dict:  # Check if the task is already in the dictionary
                tasks_dict[task].add(item['_id'])  # Adding item '_id' to the existing list
            else:
                tasks_dict[task] = {item['_id']}  # Initialize a set with the first '_id'
    
    return tasks_dict


def loadAllFiles(folderpath):
    alldata = []
    # Iterate over all JSON files in the folder
    for filename in os.listdir(folderpath):
        if filename.endswith('.json'):
            json_file = os.path.join(folderpath, filename)
            print(f"Processing file: {json_file}")
            with open(json_file, 'r') as f:
                data = json.load(f)
            
            total_entries = len(data)
            print(f"Total entries in {filename}: {total_entries}")

            alldata.extend(data)

    return alldata

def combinedValues(dt1, dt2, key):
    # Extract the values for the given key from both dt1 and dt2
    values_dt1 = extract_values(dt1, key)
    values_dt2 = extract_values(dt2, key)

    # Create an object (dictionary) that maps the ids of dt1 and dt2 to their respective values
    combined_values = {
        dt1["id"]: values_dt1,  # Map dt1's id to its extracted values
        dt2["id"]: values_dt2   # Map dt2's id to its extracted values
    }

    return combined_values

def createDatasetNetwork(tasks_dict, data):
    filename = 'output/dataset_network.json'

    delete_file(filename)

    total_tasks = len(tasks_dict)
    current_task_number = 1

    for key in tasks_dict:
        # Convert set to list for indexing
        item_list = list(tasks_dict[key])
        
        # Get the associated array size
        array_size = len(item_list)
        
        # Print progress with array size information
        print(f"Processing task {key} ({current_task_number}/{total_tasks}). Array size: {array_size}")
        
        network = []

        # Iterate over each item in the list with index
        for i, item1 in enumerate(item_list):
            # Access the item in the dictionary using the key directly
            dt1 = data.get(item1)
            if dt1:  # Check if dt1 is not None
                
                # Iterate over the subsequent items in the list
                for item2 in item_list[i + 1:]:
                    dt2 = data.get(item2)
        
                    if dt2:  # Check if dt2 is not None

                        

                        value = {
                            'date': {'value': dt1["lastModified"]},
                            'p': {'value': key},
                            's': {'value': dt1["id"]},
                            'o': {'value': dt2["id"]},
                            'label': {'value': key},
                            'modality': combinedValues(dt1, dt2, 'modality'),
                            'license': combinedValues(dt1, dt2, 'license')
                        }
                    
                        network.append(value)
            
        print(json.dumps(network[:2], indent=4))

        current_task_number += 1

        # Break after processing 2 tasks for testing
        if current_task_number == 3: 
            break

        append_json_to_file(filename, network)


def delete_file(file_path):
    # Delete the file
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"{file_path} has been deleted.")
    else:
        print(f"{file_path} does not exist.")


def append_json_to_file(file_path, new_data):
    """
    Appends a new JSON object to a file containing a JSON array. Creates the file if it does not exist.

    :param file_path: Path to the JSON file.
    :param new_data: New JSON data to append.
    """
    # Check if the file exists
    if os.path.exists(file_path):
        # Read existing data
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                if not isinstance(data, list):
                    raise ValueError("Existing JSON data is not a list.")
            except (json.JSONDecodeError, ValueError):
                # If the file is empty or contains invalid JSON, start with an empty list
                data = []
    else:
        # File does not exist, start with an empty list
        data = []

    # Append new data
    data.append(new_data)

    # Write updated data back to the file
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def writeToFile(data, filename):
    with open(filename, 'w') as outfile:
        json.dump(data, outfile, indent=4)


# Example usage
if __name__ == "__main__":
    folder_path = 'modality_datasets'  # Replace with your folder path containing JSON files
    data = loadAllFiles(folder_path)

    tasks_dict = extractTaskDict(data)

    for key in tasks_dict:
        # Get the associated array size
        print(f"{key}: {len(tasks_dict[key])} datasets" )

    data_dict = {item['_id']: item for item in data} # Transform json array into a dict to facilitate access to items
    createDatasetNetwork(tasks_dict, data_dict)
