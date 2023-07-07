from requests import get
from pokemon_node import pokemon

# Node class for the Linked List
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Linked List class
class EvolutionLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("End")

# Fetch Data from PokéAPI and Create Linked List
def create_pokemon_evolution_chain(id):
    url = f"https://pokeapi.co/api/v2/evolution-chain/{id}/"
    response = get(url)
    data = response.json()

    evolution_chain = EvolutionLinkedList()

    chain = data["chain"]
    while chain:
        species = chain["species"]["name"]
        evolution_chain.append(species.capitalize())

        if chain.get("evolves_to"):
            chain = chain["evolves_to"][0]
        else:
            chain = None

    return evolution_chain

pokemon_id = 4  # Charmander's ID
evolution_chain = create_pokemon_evolution_chain(pokemon_id)
evolution_chain.display()
