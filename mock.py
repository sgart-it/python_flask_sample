# mock.py

db = [
    {"id": 0, "title": "Home", "body": "By <a href='https://www.sgart.it'><b>sgart.it</b></a>"},
    {"id": 1, "title": "Pagina 1", "body": "corpo della <b>pagina 1</b>"},
    {"id": 2, "title": "Info", "body": "Test Flask"},
]

def get(id):
    for item in db:
        if item["id"] == id:
            print(item)
            return item
    return None

def menu():
    items = []
    for item in db:
        items.append({"id": item["id"], "title": item["title"]})
    return items