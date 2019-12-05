import json


class Pet:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    @staticmethod
    def populate_pet_list(filepath="all_pets.json"):

        with open(filepath, 'r') as f:
            data = json.load(f)

        return [
            Pet(**animal) for animal in data['pets']
        ]

