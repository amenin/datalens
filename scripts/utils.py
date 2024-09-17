### DATA FORMATING V1

# import json

# # Read the input JSON file
# input_file = '/user/aollagni/home/Documents/GitHub/MGNLP-Explorer/links_desc_task_cat.json'
# output_file = 'test.json'

# with open(input_file, 'r') as f:
#     data = json.load(f)

# # Initialize a list to store the reformatted data
# reformatted_data = []

# # Iterate over the original data and reformat it as specified
# for item in data:
#     reformatted_item = {
#         'p': {'value': item.get('weight', '')},
#         's': {'value': item.get('source', '')},
#         'o': {'value': item.get('target', '')},
#         'label': {'value': item.get('source', '')}
#     }
#     reformatted_data.append(reformatted_item)

# # Write the reformatted data to the output JSON file
# with open(output_file, 'w') as f:
#     json.dump(reformatted_data, f, indent=2)

# print(f'Reformatted data has been written to {output_file}')

### DATA FORMATING V2

# import json
# import re

# # Read the input JSON file
# input_file = '/user/aollagni/home/Documents/GitHub/MGNLP-Explorer/source/links_desc_task_cat.json'
# output_file = 'results/v2/full__desc_task_cat.json'

# # Paths to JSON files
# metadata_file = '/user/aollagni/home/Documents/GitHub/NLP-Metadata-Datasets/metadata-archive.json'
# data_file = 'source/links_desc_task_cat.json'
# output_file = 'results/v2/full__desc_task_cat.json'

# # Initialize an empty dictionary to store the data
# metadata_dict = {}

# # Read data from the JSON file and populate the dictionary
# with open(metadata_file, 'r') as f:
#     for line in f:
#         entry = json.loads(line)
#         entry_id = entry.get('id', None)
#         if entry_id:
#             metadata_dict[entry_id] = entry

# # List of keys to check for emptiness
# keys_to_check = ['description', 'categories', 'tasks']

# # Create a copy of the dictionary to avoid modifying the original data
# filtered_metadata_dict = metadata_dict.copy()

# # Iterate through the dictionary and remove entries where specified keys are empty
# for entry_id, entry_data in metadata_dict.items():
#     for key in keys_to_check:
#         if not entry_data['data'].get(key):
#             del filtered_metadata_dict[entry_id]
#             break

# # Print the total number of remaining entries
# print(f"Total remaining entries: {len(filtered_metadata_dict)}")

# # Initialize a new dictionary to store the filtered data
# filtered_metadata_dict_filtered = {}

# # Iterate through filtered_metadata_dict
# for entry_id, entry_data in filtered_metadata_dict.items():
#     data = entry_data['data']
    
#     # Extract data for reshaping
#     author_description = data.get('description', '')
#     author_url = data.get('url', '')
#     author_license = data.get('givenLicense', '')
#     author_language = ', '.join(data.get('language', []))
#     author_categories = ', '.join(data.get('categories', []))
#     author_tasks = ', '.join(data.get('tasks', []))


#     filtered_metadata_dict_filtered[entry_id] = entry_data

#     # Create the reshaped author_list_str
#     author_list_str = f"Description: {author_description}, " \
#                     f"URL: {author_url}, " \
#                     f"License: {author_license}, " \
#                     f"Language: {author_language}, " \
#                     f"Categories: {author_categories}, " \
#                     f"Tasks: {author_tasks}"
    
#     # Add author_list_str to the data dictionary
#     filtered_metadata_dict_filtered[entry_id]['data']['author_list_str'] = author_list_str

# # Print the total number of remaining entries
# print(f"Total remaining entries: {len(filtered_metadata_dict_filtered)}")

# # Threshold for weight
# threshold = 0.87  # Adjust as needed

# # Initialize a list to store the results
# results = []

# # Initialize a list to store the reformatted data
# reformatted_data = []


# # Read data from the second JSON file (assuming it's a list of JSON objects)
# with open(data_file, 'r') as data_f:
#     data_entries = json.load(data_f)

#     # Iterate through the data entries
#     for data_entry in data_entries:
#         source = data_entry.get('source', '')
#         target = data_entry.get('target', '')
#         weight = data_entry.get('weight', 0.0)

#         # Check if "source" and "target" are different, weight is above the threshold, and "source" exists in filtered_metadata_dict_filtered
#         if source != target and weight > threshold and source in filtered_metadata_dict_filtered and target in filtered_metadata_dict_filtered:
            
#             # Get the "author_list_str" for the source from filtered_metadata_dict_filtered
#             author_list_str = filtered_metadata_dict_filtered[source]['data']['author_list_str']

#             # Concatenate Categories and Tasks of the given entry
#             entry_data = filtered_metadata_dict_filtered[source]['data']
#             categories = ', '.join(entry_data.get('categories', []))
#             tasks = ', '.join(entry_data.get('tasks', []))
#             concatenated_categories_tasks = ', '.join(filter(None, [categories, tasks]))

#             reformatted_item = {
#                 'p': {'value': concatenated_categories_tasks},
#                 's': {'value': source},
#                 'o': {'value': data_entry['target']},
#                 'label': {'value': f"{concatenated_categories_tasks} ({weight})"},
#                 'authorList': {'value': author_list_str}
#             }
#             reformatted_data.append(reformatted_item)

# # Write the results to a JSON file
# with open(output_file, 'w') as f:
#     json.dump(reformatted_data, f, indent=2)

# print(f'Reformatted data has been written to {output_file}')

### TASK AND CATEGORY LISTING

# import json

# # Define the path to the JSON file
# second_input_file = '/user/aollagni/home/Documents/GitHub/NLP-Metadata-Datasets/metadata-archive.json'

# # Initialize empty sets to store unique task and category values
# unique_tasks = set()
# unique_categories = set()

# # Read data from the JSON file
# with open(second_input_file, 'r') as f:
#     for line in f:
#         item = json.loads(line)
        
#         # Extract 'task' and 'category' values and add them to the sets
#         task = item.get('data', {}).get('tasks', [])
#         category = item.get('data', {}).get('categories', [])
        
#         unique_tasks.update(task)
#         unique_categories.update(category)

# # Convert the sets to lists if needed
# unique_tasks_list = list(unique_tasks)
# unique_categories_list = list(unique_categories)

# # Print the unique task and category values
# print("Unique Task Values:")
# for task in unique_tasks_list:
#     print(task)

# print("\nUnique Category Values:")
# for category in unique_categories_list:
#     print(category)

# ### VISU GRAPH

import json
import re

# List of labels to search for
image_classification_list = [
    "image-classification",
    "object-detection",
    "image-segmentation",
    "visual-question-answering",
    "image-to-text",
    "image-captioning",
    "instance-segmentation",
    "other-scene-parsing"
]

# Paths to JSON files
metadata_file = '/user/aollagni/home/Documents/GitHub/NLP-Metadata-Datasets/metadata-archive.json'
data_file = 'source/links_desc.json'
output_file = 'results/v3/visu/sim_links_tasks.json'

# Initialize an empty dictionary to store the data
metadata_dict = {}

# Read data from the JSON file and populate the dictionary
with open(metadata_file, 'r') as f:
    for line in f:
        entry = json.loads(line)
        entry_id = entry.get('id', None)
        if entry_id:
            metadata_dict[entry_id] = entry

# List of keys to check for emptiness
keys_to_check = ['tasks']#, 'categories', 'tasks']

# Create a copy of the dictionary to avoid modifying the original data
filtered_metadata_dict = metadata_dict.copy()

# Iterate through the dictionary and remove entries where specified keys are empty
for entry_id, entry_data in metadata_dict.items():
    for key in keys_to_check:
        if not entry_data['data'].get(key):
            del filtered_metadata_dict[entry_id]
            break

# Print the total number of remaining entries
print(f"Total remaining entries: {len(filtered_metadata_dict)}")

# Initialize a new dictionary to store the filtered data
filtered_metadata_dict_filtered = {}

# Iterate through filtered_metadata_dict
for entry_id, entry_data in filtered_metadata_dict.items():
    data = entry_data['data']
    
    # Extract data for reshaping
    author_description = data.get('description', '')
    author_url = data.get('url', '')
    author_license = data.get('givenLicense', '')
    author_language = ', '.join(data.get('language', []))
    author_categories = ', '.join(data.get('categories', []))
    author_tasks = ', '.join(data.get('tasks', []))

        # Check if any label matches in author_categories or author_tasks
    if any(label in image_classification_list for label in author_categories.split(', ') + author_tasks.split(', ')):
        # Add the entry to the filtered dictionary
        filtered_metadata_dict_filtered[entry_id] = entry_data
    
        # Create the reshaped author_list_str
        author_list_str = f"Description: {author_description}, " \
                        f"URL: {author_url}, " \
                        f"License: {author_license}, " \
                        f"Language: {author_language}, " \
                        f"Categories: {author_categories}, " \
                        f"Tasks: {author_tasks}"
        
        # Add author_list_str to the data dictionary
        filtered_metadata_dict_filtered[entry_id]['data']['author_list_str'] = author_list_str

# Print the total number of remaining entries
print(f"Total remaining entries: {len(filtered_metadata_dict_filtered)}")

# Threshold for weight
threshold = 0.87  # Adjust as needed

# Initialize a list to store the results
results = []

# Initialize a list to store the reformatted data
reformatted_data = []


# Read data from the second JSON file (assuming it's a list of JSON objects)
with open(data_file, 'r') as data_f:
    data_entries = json.load(data_f)

    # Iterate through the data entries
    for data_entry in data_entries:
        source = data_entry.get('source', '')
        target = data_entry.get('target', '')
        weight = data_entry.get('weight', 0.0)

        # Check if "source" and "target" are different, weight is above the threshold, and "source" exists in filtered_metadata_dict_filtered
        if source != target and weight > threshold and source in filtered_metadata_dict_filtered and target in filtered_metadata_dict_filtered:
            
            # Get the "author_list_str" for the source from filtered_metadata_dict_filtered
            author_list_str = filtered_metadata_dict_filtered[source]['data']['author_list_str']

            # Concatenate Categories and Tasks of the given entry
            entry_data = filtered_metadata_dict_filtered[source]['data']
            categories = ', '.join(entry_data.get('categories', []))
            tasks = ', '.join(entry_data.get('tasks', []))
            #concatenated_categories_tasks = ', '.join(filter(None, [categories, tasks]))

            reformatted_item = {
                'p': {'value': tasks},
                's': {'value': source},
                'o': {'value': data_entry['target']},
                'label': {'value': f"{entry_data.get('description', '')} ({weight})"},
                'authorList': {'value': author_list_str}
            }
            reformatted_data.append(reformatted_item)

# Write the results to a JSON file
with open(output_file, 'w') as f:
    json.dump(reformatted_data, f, indent=2)

print(f'Reformatted data has been written to {output_file}')

### SPEECH GRAPH

# import json

# # List of labels to search for
# audio_list = [
#     "automatic-speech-recognition",
#     "audio-classification",
#     "audio-speaker-identification",
#     "audio-classification",
#     "audio-emotion-recognition",
#     "speaker-language-identification",
#     "audio-classification-other-automatic-speaker-verification",
#     "audio-classification-other-query-by-example-spoken-term-detection",
#     "audio-classification-other-speaker-diarization",
#     "other-audio-slot-filling",
# ]


# # Paths to JSON files
# metadata_file = '/user/aollagni/home/Documents/GitHub/NLP-Metadata-Datasets/metadata-archive.json'
# data_file = 'source/links_desc.json'
# output_file = 'results/v3/speech/sim_links_categories.json'

# # Initialize an empty dictionary to store the data
# metadata_dict = {}

# # Read data from the JSON file and populate the dictionary
# with open(metadata_file, 'r') as f:
#     for line in f:
#         entry = json.loads(line)
#         entry_id = entry.get('id', None)
#         if entry_id:
#             metadata_dict[entry_id] = entry

# # List of keys to check for emptiness
# keys_to_check = ['categories']#, 'categories', 'tasks']

# # Create a copy of the dictionary to avoid modifying the original data
# filtered_metadata_dict = metadata_dict.copy()

# # Iterate through the dictionary and remove entries where specified keys are empty
# for entry_id, entry_data in metadata_dict.items():
#     for key in keys_to_check:
#         if not entry_data['data'].get(key):
#             del filtered_metadata_dict[entry_id]
#             break

# # Print the total number of remaining entries
# print(f"Total remaining entries: {len(filtered_metadata_dict)}")

# # Initialize a new dictionary to store the filtered data
# filtered_metadata_dict_filtered = {}

# # Iterate through filtered_metadata_dict
# for entry_id, entry_data in filtered_metadata_dict.items():
#     data = entry_data['data']
    
#     # Extract data for reshaping
#     author_description = data.get('description', '')
#     author_url = data.get('url', '')
#     author_license = data.get('givenLicense', '')
#     author_language = ', '.join(data.get('language', []))
#     author_categories = ', '.join(data.get('categories', []))
#     author_tasks = ', '.join(data.get('tasks', []))

#         # Check if any label matches in author_categories or author_tasks
#     if any(label in audio_list for label in author_categories.split(', ') + author_tasks.split(', ')):
#         # Add the entry to the filtered dictionary
#         filtered_metadata_dict_filtered[entry_id] = entry_data
    
#         # Create the reshaped author_list_str
#         author_list_str = f"Description: {author_description}, " \
#                         f"URL: {author_url}, " \
#                         f"License: {author_license}, " \
#                         f"Language: {author_language}, " \
#                         f"Categories: {author_categories}, " \
#                         f"Tasks: {author_tasks}"
        
#         # Add author_list_str to the data dictionary
#         filtered_metadata_dict_filtered[entry_id]['data']['author_list_str'] = author_list_str

# # Print the total number of remaining entries
# print(f"Total remaining entries: {len(filtered_metadata_dict_filtered)}")

# # Threshold for weight
# threshold = 0.87  # Adjust as needed

# # Initialize a list to store the results
# results = []

# # Initialize a list to store the reformatted data
# reformatted_data = []


# # Read data from the second JSON file (assuming it's a list of JSON objects)
# with open(data_file, 'r') as data_f:
#     data_entries = json.load(data_f)

#     # Iterate through the data entries
#     for data_entry in data_entries:
#         source = data_entry.get('source', '')
#         target = data_entry.get('target', '')
#         weight = data_entry.get('weight', 0.0)

#         # Check if "source" and "target" are different, weight is above the threshold, and "source" exists in filtered_metadata_dict_filtered
#         if source != target and weight > threshold and source in filtered_metadata_dict_filtered and target in filtered_metadata_dict_filtered:
            
#             # Get the "author_list_str" for the source from filtered_metadata_dict_filtered
#             author_list_str = filtered_metadata_dict_filtered[source]['data']['author_list_str']

#             # Concatenate Categories and Tasks of the given entry
#             entry_data = filtered_metadata_dict_filtered[source]['data']
#             categories = ', '.join(entry_data.get('categories', []))
#             tasks = ', '.join(entry_data.get('tasks', []))
#             concatenated_categories_tasks = ', '.join(filter(None, [categories, tasks]))

#             reformatted_item = {
#                 'p': {'value': categories},
#                 's': {'value': source},
#                 'o': {'value': data_entry['target']},
#                 'label': {'value': f"{entry_data.get('description', '')} ({weight})"},
#                 'authorList': {'value': author_list_str}
#             }
#             reformatted_data.append(reformatted_item)

# # Write the results to a JSON file
# with open(output_file, 'w') as f:
#     json.dump(reformatted_data, f, indent=2)

# print(f'Reformatted data has been written to {output_file}')

### TEXT GRAPH

# import json

# # # List of labels to search for
# nlp_tasks_list = [
#     "explanation-generation",
#     "text-generation-other-discourse-analysis",
#     "multiple-choice",
#     "text-scoring",
#     "table-to-text",
#     "translation",
#     "token-classification",
#     "text-generation",
#     "other-text-search",
#     "tabular-to-text",
#     "text-generation-other-common-sense-inference",
#     "text-classification",
#     "visual-question-answering",
#     "question-answering",
#     "image-to-text",
#     "conversational",
#     "text-retrieval",
#     "text-to-tabular",
#     "text-to-structured",
#     "text-generation-other-code-modeling",
#     "summarization",
#     "text2text-generation",
#     "zero-shot-classification",
#     "sequence-modeling",
#     "fill-mask",
#     "summarization-other-aspect-based-summarization",
#     "question-answering-other-multi-hop",
#     "masked-language-modeling",
#     "text-classification-other-dialogue-sentiment-classification",
#     "other-other-text-to-speech",
#     "other-other-citation-recommendation",
#     "other-other-story-completion",
#     "question-ansering-other-dialogue-qa",
#     "text-scoring",
#     "sentiment-analysis",
#     "word-sense-disambiguation",
#     "text-classification-other-headline-grouping",
#     "univariate-time-series-forecasting",
#     "text-classification-other-hate-speech-topic-classification",
#     "other-other-open-information-extraction",
#     "other-text-search",
#     "parsing",
#     "text-classification-other-rationale-extraction",
#     "other-dialogue-state-tracking",
#     "other-neural-search",
#     "multiple-choice-qa",
#     "semantic-similarity-classification",
#     "text-classification-other-narrative-flow",
#     "text2text-generation-other-meaning-representation-to-text",
#     "text-classification-other-social-media-shares-prediction",
#     "text-classification-other-evaluating-dialogue-systems",
#     "text-classification-other-offensive-language-classification",
#     "semantic-similarity-scoring",
#     "token-classification-other-keyphrase-extraction",
#     "text2text-generation-other-meaning-representtion-to-text",
#     "other-compositionality",
#     "text-classification-other-gender-bias",
#     "multi-input-text-classification",
#     "topic-classification",
#     "text-classification-other-hope-speech-classification",
#     "summarization-other-conversations-summarization",
#     "token-classification-other-word-tokenization",
#     "other-other-token-classification-of-text-errors",
#     "closed-domain-qa",
#     "text-classification-other-language-identification",
#     "text-retrieval-other-parallel-sentence-retrieval",
#     "token-classification-other-word-segmentation",
#     "text2text-generation-other-math-word-problems",
#     "question-answering-other-chained-qa",
#     "semantic-role-labeling",
#     "summarization-other-bills-summarization",
#     "utterance-retrieval",
#     "token-classification-other-constituency-parsing",
#     "text-classification-other-judgement-prediction",
#     "abstractive-qa",
#     "token-classification-other-fused-head-identification",
#     "summarization--other-headline-generation",
#     "token-classification-other-sentence-segmentation",
#     "question-answering-other-explanations-in-question-answering",
#     "question-answering-other-yes-no-qa",
#     "text-simplification",
#     "translation-other-text-to-code",
#     "text-classification-other-funniness-score-prediction",
#     "summarization-other-paper-abstract-generation",
#     "other-other-digital-humanities-research",
#     "other-other-web-search",
#     "text-classification-other-funnier-headline-identification",
#     "text-classification-other-stance-detection",
#     "other-diacritics-prediction",
#     "text-classification-other-bias-evaluation",
#     "text2text-generation-other-long-range-dependency",
#     "token-classification-other-propaganda-span-identification",
#     "language-modeling",
#     "text-classification-other-translation-quality-estimation",
#     "text-classification-legal-topic-classification",
#     "text-classification-other-question-answer-pair-classification",
#     "multi-class-classification",
#     "question-answering-other-generative-reading-comprehension-metric",
#     "text-scoring-other-evaluating-dialogue-systems",
#     "intent-classification",
#     "token-classification-other-lemmatization",
#     "summarization",
#     "token-classification-other-relation-prediction",
#     "question-answering-other-conversational-qa",
#     "token-classification-other-acronym-identification",
#     "other-other-knowledge-base",
#     "summarization-other-reddit-posts-summarization",
#     "text2text-generation-other-intent-to-text",
#     "text-generation",
#     "text-classification-other-hate-speech-detection",
#     "text2text-generation-other-poem-generation",
#     "text-classification-other-simplification-evaluation",
#     "text2text-generation-other-explanation-generation",
#     "text-classification-other-aspect-based-sentiment-analysis",
#     "other-other-NCI-PID-PubMed",
#     "text2text-generation-other-question-generation",
#     "translation-other-code-documentation-translation",
#     "other-other-contextual-embeddings",
#     "summarization-other-extractive-summarization",
#     "fact-checking",
#     "other-multi-turn",
#     "other-other-data-mining",
#     "text-classification-other-qa-nli",
#     "part-of-speech-tagging",
#     "token-classification-other-dependency-parsing",
#     "text-classification-other-discourse-marker-prediction",
#     "named-entity-recognition",
#     "rdf-to-text",
#     "token-classification-other-conversation-disentanglement",
#     "multi-label-image-classification",
#     "text-classification-other-coreference-nli",
#     "text-classification-other-Meronym-Prediction",
#     "multi-class-image-classification",
#     "dialogue-modeling",
#     "keyword-spotting",
#     "token-classification-other-clause-segmentation",
#     "other-other-sentences",
#     "dialogue-generation",
#     "text2text-generation-other-concepts-to-text",
#     "token-classification-other-span-extraction",
#     "question-answering-other-knowledge-base-qa",
#     "text-classification-other-toxicity-prediction",
#     "token-classification-other-morphology",
#     "question-answering-other-table-question-answering",
#     "other-other-Conversational",
#     "entity-linking-retrieval",
#     "text-classification-other-Hate",
#     "translation-other-code-to-code",
#     "summarization-other-hallucinations",
#     "lemmatization",
#     "text-classification-other-Hope",
#     "news-articles-headline-generation",
#     "coreference-resolution",
#     "text-classification-other-Word",
#     "token-classification-other-output-structure",
#     "other-concepts-to-text",
#     "news-articles-summarization",
#     "question-answering-other-multihop-tabular-text-qa",
#     "summarization-other-patent-summarization",
#     "slot-filling",
#     "text-classification-other-offensive-language",
#     "text-classification-other-sarcasm-detection",
#     "question-answering-other-zero-shot-relation-extraction",
#     "summarization-other-multi-document-summarization",
#     "text-classification-other-legal-judgment-prediction",
#     "other-other-translation",
#     "text-retrieval-other-document-to-document-retrieval",
#     "other-intent-to-text",
#     "text-classification-other-news-category-classification",
#     "text2text-generation-other-paraphrase-generation",
#     "open-domain-qa",
#     "text-classification-other-emotion-classification"
# ]

# # Paths to JSON files
# metadata_file = '/user/aollagni/home/Documents/GitHub/NLP-Metadata-Datasets/metadata-archive.json'
# data_file = 'source/links_desc.json'
# output_file = 'results/v3/text/sim_links_categories.json'  ###########

# # Initialize an empty dictionary to store the data
# metadata_dict = {}

# # Read data from the JSON file and populate the dictionary
# with open(metadata_file, 'r') as f:
#     for line in f:
#         entry = json.loads(line)
#         entry_id = entry.get('id', None)
#         if entry_id:
#             metadata_dict[entry_id] = entry

# # List of keys to check for emptiness
# keys_to_check = ['categories']#, 'categories', 'tasks'] #################

# # Create a copy of the dictionary to avoid modifying the original data
# filtered_metadata_dict = metadata_dict.copy()

# # Iterate through the dictionary and remove entries where specified keys are empty
# for entry_id, entry_data in metadata_dict.items():
#     for key in keys_to_check:
#         if not entry_data['data'].get(key):
#             del filtered_metadata_dict[entry_id]
#             break

# # Print the total number of remaining entries
# print(f"Total remaining entries: {len(filtered_metadata_dict)}")

# # Initialize a new dictionary to store the filtered data
# filtered_metadata_dict_filtered = {}

# # Iterate through filtered_metadata_dict
# for entry_id, entry_data in filtered_metadata_dict.items():
#     data = entry_data['data']
    
#     # Extract data for reshaping
#     author_description = data.get('description', '')
#     author_url = data.get('url', '')
#     author_license = data.get('givenLicense', '')
#     author_language = ', '.join(data.get('language', []))
#     author_categories = ', '.join(data.get('categories', []))
#     author_tasks = ', '.join(data.get('tasks', []))

#         # Check if any label matches in author_categories or author_tasks
#     if any(label in nlp_tasks_list for label in author_categories.split(', ') + author_tasks.split(', ')):
#         # Add the entry to the filtered dictionary
#         filtered_metadata_dict_filtered[entry_id] = entry_data
    
#         # Create the reshaped author_list_str
#         author_list_str = f"Description: {author_description}, " \
#                         f"URL: {author_url}, " \
#                         f"License: {author_license}, " \
#                         f"Language: {author_language}, " \
#                         f"Categories: {author_categories}, " \
#                         f"Tasks: {author_tasks}"
        
#         # Add author_list_str to the data dictionary
#         filtered_metadata_dict_filtered[entry_id]['data']['author_list_str'] = author_list_str

# # Print the total number of remaining entries
# print(f"Total remaining entries: {len(filtered_metadata_dict_filtered)}")

# # Threshold for weight
# threshold = 0.87  # Adjust as needed

# # Initialize a list to store the results
# results = []

# # Initialize a list to store the reformatted data
# reformatted_data = []


# # Read data from the second JSON file (assuming it's a list of JSON objects)
# with open(data_file, 'r') as data_f:
#     data_entries = json.load(data_f)

#     # Iterate through the data entries
#     for data_entry in data_entries:
#         source = data_entry.get('source', '')
#         target = data_entry.get('target', '')
#         weight = data_entry.get('weight', 0.0)

#         # Check if "source" and "target" are different, weight is above the threshold, and "source" exists in filtered_metadata_dict_filtered
#         if source != target and weight > threshold and source in filtered_metadata_dict_filtered and target in filtered_metadata_dict_filtered:
            
#             # Get the "author_list_str" for the source from filtered_metadata_dict_filtered
#             author_list_str = filtered_metadata_dict_filtered[source]['data']['author_list_str']

#             # Concatenate Categories and Tasks of the given entry
#             entry_data = filtered_metadata_dict_filtered[source]['data']
#             categories = ', '.join(entry_data.get('categories', []))
#             tasks = ', '.join(entry_data.get('tasks', []))
#             concatenated_categories_tasks = ', '.join(filter(None, [categories, tasks]))

#             reformatted_item = {
#                 'p': {'value': categories}, ##############
#                 's': {'value': source},
#                 'o': {'value': data_entry['target']},
#                 'label': {'value': f"{entry_data.get('description', '')} ({weight})"},
#                 'authorList': {'value': author_list_str}
#             }
#             reformatted_data.append(reformatted_item)

# # Write the results to a JSON file
# with open(output_file, 'w') as f:
#     json.dump(reformatted_data, f, indent=2)

# print(f'Reformatted data has been written to {output_file}')