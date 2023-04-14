# INFOVIZ - Data Lineage Visualization

This Django project provides a data lineage visualization tool for tables in a multi hop architecture. 
It allows you to visually explore and understand the relationships between different tables in your data lake.

## Features

- Visualizes data lineage for tables in a multi hop architecture, provided records in csv file - infoviz/graph/media/csv/tables.csv
- Display tables and their relationships using a network visualization.
- Supports filtering and highlighting of tables and their connections.
- Provide options for customizing node and edge appearance.
- Allows for interactive exploration of the data lineage graph.

## Requirements

- Python 3.9
- Django 4.1
- vis.js (JavaScript library for network visualization)
- vis-network (Python library for integrating vis.js with Django)

## Installation

1. Clone this repository to your local machine:

```sh
git clone https://github.com/SonawaneMayur/django-data-lineage.git
```


2.Install the required Python packages using pip:
```sh
pip install -r requirements.txt
```

3.include vis.js library in your Django project. You can download it from the official website (https://visjs.org/) and place it in your project's static files directory.

4.Update the Django project settings to include the vis-network app in the INSTALLED_APPS setting:

```python
INSTALLED_APPS = [
    # ...
    'graph',
    # ...
]

```
5.Run Django migrations:

```shell
python manage.py makemigrations
python manage.py migrate
```
6.Start the Django development server:
```shell
python manage.py runserver
```

7.Open your web browser and go to http://localhost:8000 to access the data lineage visualization tool.


##Usage
1.Use the data lineage visualization tool to explore the relationships between tables in your data lake.
2.Use the filter and highlighting options to focus on specific tables or connections.
3.Customize the appearance of nodes and edges by updating the settings in your HTML file.
4.Interact with the visualization to zoom, pan, and select nodes or edges for more information.


##License
MIT License

Copyright (c) [2023] [Mayur Sonawane]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.