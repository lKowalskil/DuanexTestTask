import json
import os

file_path = 'test.json'

sounds = {
    'dog': 'bark',
    'cat': 'meow',
    'cow': 'moo',
    'rat': 'pipi',
    'alien': 'KILL'
}

if not os.path.exists(file_path):
    print(f"Error: File '{file_path}' does not exist.")
else:
    try:
        with open(file_path) as file:
            data = json.load(file)
        
        if 'animal' not in data:
            print("Error: 'animal' field is missing in the JSON file.")
        else:
            animal = data['animal']

            if animal in sounds:
                print(sounds[animal])
            else:
                print(f"Error: Unknown animal '{animal}'. Valid options are: {', '.join(sounds.keys())}.")
    
    except json.JSONDecodeError:
        print("Error: Failed to parse JSON file.")
