import json
import xml.etree.ElementTree as et

class Animals:
    def __init__(self, name, eat, color):
        self.name = name
        self.eat = eat
        self.color = color

class AnimalsAbout:
    def About(self, name, format):
        if format == 'JSON':
            animal_info = {
                'name': name.name,
                'eat': name.eat,
                'color': name.color
            }
        elif format == 'XML':
            animal_info = et.Element('name', attrib={'name': name.name})
            eat = et.SubElement(animal_info, 'eat')
            eat.text = name.eat
            color = et.SubElement(animal_info, 'color')
            color.text = name.color
            return et.tostring(animal_info, encoding='unicode')
        else:
            raise ValueError(format)

class Exseptions(Animals):
    try:
        number_of_animal = int(input("Порядковый номер животного: "))
        if number_of_animal > 0:
            print(number_of_animal)
        else:
            print(error)
    except Exseptions as e:
        print(e)

