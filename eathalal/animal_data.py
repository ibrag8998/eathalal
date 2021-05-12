import json
from typing import List, Optional, FrozenSet


class Animal:
    def __init__(self, name: str, is_halal: Optional[bool], comment: str) -> None:
        self.name = name
        self.is_halal = is_halal
        self.comment = comment


class AnimalCollection:
    def __init__(self) -> None:
        self._animals: FrozenSet[Animal] = frozenset(self.read_json())

    def read_json(self) -> List[Animal]:
        with open('eathalal/data.json') as f:
            return json.load(f, object_hook=lambda d: Animal(**d))

    def search(self, animal_name: str):
        for animal in self._animals:
            if animal_name.lower() in animal.name:
                yield animal


animals = AnimalCollection()
