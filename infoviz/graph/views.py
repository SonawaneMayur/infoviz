import csv
import json
import uuid

from django.shortcuts import render

src_lvl = [0, 1, 2]
trgt_lvl = [1, 2, 3]


def graph(request):
    # Check if a file was uploaded
    if request.method == "POST" and request.FILES["file"]:
        # Get the uploaded file
        file = request.FILES["file"]

        decoded_file = file.read().decode('utf-8')
        # Read the CSV data
        # data = csv.DictReader(file)
        reader = csv.reader(decoded_file.splitlines(), delimiter=',')
        # Create nodes and links dictionaries
        nodes = {}
        edges = []
        for row in reader:
            source, job, target = row
            if source not in nodes:
                # nodes[source] = {"name": source}
                source_id = str(uuid.uuid4())
                source_lvl = 0  # random.choice(src_lvl)
                nodes[source] = {"id": source_id, "label": source, "level": source_lvl, "props": []}
            if target not in nodes:
                # nodes[target] = {"name": target}
                target_id = str(uuid.uuid4())
                target_lvl = nodes[source]["level"] + 1  # random.choice([i for i in trgt_lvl if i > source_lvl])
                nodes[target] = {"id": target_id, "label": target, "level": target_lvl}
            edges.append({"from": nodes[source]["id"], "to": nodes[target]["id"], "label": job})
        # Create the JSON data
        graph_data = {"nodes": list(nodes.values()), "edges": edges}

        print(graph_data)
        # Render the graph template with the graph data
        return render(request, "static.html", {"graph_data": json.dumps(graph_data)})
    # If no file was uploaded, render the upload template
    return render(request, "upload.html")
