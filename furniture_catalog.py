def suggest_furniture(room):

    catalog = {

        "bedroom": [
            "king bed",
            "nightstand",
            "wardrobe",
            "bedside lamp",
            "dresser"
        ],

        "living room": [
            "sofa",
            "coffee table",
            "tv unit",
            "bookshelf",
            "floor lamp"
        ],

        "kitchen": [
            "kitchen island",
            "bar stools",
            "modern cabinets",
            "hanging lights"
        ],

        "office": [
            "desk",
            "ergonomic chair",
            "bookshelf",
            "desk lamp"
        ]
    }

    return catalog.get(room, [])
