from jinja2 import Environment, FileSystemLoader

with open("main.html.j2", "r") as f:
    htmlString = f.read()

data = {
    "name": "Jake"
}

load = FileSystemLoader(".")
template = Environment(loader=load).from_string(htmlString)
htmlOutput = template.render(**data)

with open("renderedExample.html", "w") as f:
    f.write(htmlOutput)
