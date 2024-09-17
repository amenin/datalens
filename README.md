# MGNLP-Explorer README

Welcome to the MGNLP-Explorer, a powerful tool designed for visualizing Natural Language Processing (NLP) resources. Our tool allows you to navigate and understand NLP datasets by creating node-like structures based on the similarities computed from aggregated dataset information.

# Repository Contents

Here's a breakdown of the contents in this repository:

## Source

This directory contains the essential sources used to build visualizations with node-like structures. These structures are constructed based on the similarities computed from various dataset information aggregation.

## Results

### V1

In this directory, you'll find formatted JSON files that are specifically tailored to meet the MG EXPLORER specifications. In this specific version "p" and "label" contain respectively the degree of similarities between datasets and the name of the source dataset.

    results/v1/full__desc_desc.json: This JSON file contains links between datasets that are computed using similarities derived solely from the "description" label.

    results/v1/full__desc_cat.json: Similar to the previous file, this JSON file contains links between datasets. However, the similarities are computed from both the "description" and "category" labels.

    results/v1/full__desc_task.json: In this JSON file, you'll discover links between datasets. These links are computed using similarities between the "description" and "task" labels.

    results/v1/full__desc_task_cat.json: Finally, this JSON file holds links between datasets. The similarities are computed from a combination of the "description," "category," and "task" labels.

Visualizations are also available regarding each modality of language: TEXT / SPEECH / AUDIO (only one query available for each, similarities computed from a combination of the "description," "category," and "task" labels.)

    results/v1/speech/sim_links_desc_task_cat.json: JSON files providing the formatted file to visualize datasets related to speech tasks.

    results/v1/text/sim_links_desc_task_cat.json: JSON files providing the formatted file to visualize datasets related to text tasks.

    results/v1/visu/sim_links_desc_task_cat.json: JSON files providing the formatted file to visualize datasets related to text tasks.

### V2

In this directory, you'll find formatted JSON files that are specifically tailored to meet the MG EXPLORER specifications. In this specific version "p" and "label" contain both task and category information related to the source dataset as well as the degree of similarity between the given datasets.

    results/v2/full__desc_desc.json: This JSON file contains links between datasets that are computed using similarities derived solely from the "description" label.

    results/v2/full__desc_cat.json: Similar to the previous file, this JSON file contains links between datasets. However, the similarities are computed from both the "description" and "category" labels.

    results/v2/full__desc_task.json: In this JSON file, you'll discover links between datasets. These links are computed using similarities between the "description" and "task" labels.

    results/v2/full__desc_task_cat.json: Finally, this JSON file holds links between datasets. The similarities are computed from a combination of the "description," "category," and "task" labels.

Visualizations are also available regarding each modality of language: TEXT / SPEECH / AUDIO (only one query available for each, similarities computed from a combination of the "description," "category," and "task" labels.)

    results/v2/speech/sim_links_desc_task_cat.json: JSON files providing the formatted file to visualize datasets related to speech tasks.

    results/v2/text/sim_links_desc_task_cat.json: JSON files providing the formatted file to visualize datasets related to text tasks.

    results/v2/visu/sim_links_desc_task_cat.json: JSON files providing the formatted file to visualize datasets related to text tasks.

### V3

* results/v3/full__desc.json
* results/v3/visu/sim_links_desc.json
* results/v3/text/sim_links_desc.json
* results/v3/speech/sim_links_desc.json

[
   "p": {
      "value": description
    },
    "s": {
      "value": db source
    },
    "o": {
      "value": db target
    },
    "label": {
      "value": description
    },
    "authorList": {
      "value": full db description
    }

]

* results/v3/text/full_task.json
* results/v3/visu/full_task.json
* results/v3/speech/full_task.json

[
   "p": {
      "value": "task name"
    },
    "s": {
      "value": "db"
    },
    "o": {
      "value": "task name"
    },
    "label": {
      "value": "db"
    },
    "authorList": {
      "value": "info on the db like before"
    },
    "style1": {
      "value": "db"
    },
    "style2": {
        "value": "task"
    }
]

* results/v3/speech/full_category.json
* results/v3/text/full_category.json
* results/v3/visu/full_category.json

[
       "p": {
      "value": "category name"
    },
    "s": {
      "value": "db"
    },
    "o": {
      "value": "category name"
    },
    "label": {
      "value": "db"
    },
    "authorList": {
      "value": "info on the db like before"
    },
    "style1": {
      "value": "db"
    },
    "style2": {
        "value": "category"
    }
]

### V4

* results/v4/full__desc.json
* results/v4/visu/sim_links_desc.json
* results/v4/text/sim_links_desc.json
* results/v4/speech/sim_links_desc.json

[
   "p": {
      "value": description
    },
    "s": {
      "value": db source
    },
    "o": {
      "value": db target
    },
    "label": {
      "value": description
    },
    "authorList": {
      "value": full db description
    }

]

* results/v4/text/full_task.json
* results/v4/visu/full_task.json
* results/v4/speech/full_task.json

[
"p": {
      "value": "valeur de similarité"
    },
    "s": {
      "value": "db1"
    },
    "o": {
      "value": "db2"
    },
    "label": {
      "value": "category name"
    }
]

* results/v4/speech/full_category.json
* results/v4/text/full_category.json
* results/v4/visu/full_category.json

[
 "p": {
      "value": "category name"
    },
    "s": {
      "value": "db1"
    },
    "o": {
      "value": "db2"
    },
    "label": {
      "value": "category name"
    }
]

Please note that a threshold of 0.87 has been applied to these files, which ensures that only links above this similarity limit are included. This threshold helps you focus on the most relevant and similar dataset relationships.

We hope MGNLP-Explorer will prove to be a valuable resource for your NLP research and exploration. If you have any questions or need further assistance, please don't hesitate to reach out. Happy exploring!
