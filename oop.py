from abc import ABC, abstractmethod
import json
import os

class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "bark"

class Cat(Animal):
    def make_sound(self):
        return "meow"

class Cow(Animal):
    def make_sound(self):
        return "moo"

class Rat(Animal):
    def make_sound(self):
        return "pipi"

class Alien(Animal):
    def make_sound(self):
        return "KILL"

class AnimalFactory:
    @staticmethod
    def create_animal(animal_type):
        animals = {
            'dog': Dog,
            'cat': Cat,
            'cow': Cow,
            'rat': Rat,
            'alien': Alien
        }
        return animals.get(animal_type, lambda: None)()

file_path = 'test.json'

if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' does not exist.")
else:
    try:
        with open(file_path) as file:
            data = json.load(file)
        if 'animal' not in data:
            print("Error: 'animal' field is missing in the JSON file.")
        else:
            animal_type = data['animal']

            animal = AnimalFactory.create_animal(animal_type)
            if animal:
                print(animal.make_sound())
            else:
                print(f"Error: Unknown animal '{animal_type}'. Valid options are: dog, cat, cow, rat, alien.")
    
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON file.")
