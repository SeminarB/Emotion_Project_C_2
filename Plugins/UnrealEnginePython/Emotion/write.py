import json

books = {
    "name": "comic2",
    "price": "800"
}

with open('C:/xampp/htdocs/Emotion/books.json', 'w') as f:
        json.dump(books, f, indent=4)

