class Person:
    def __init__(self, name, gender, bio, is_public):
        self.name = name
        self.gender = gender
        self.bio = bio
        self.is_public = is_public

class UDGraph:
    def __init__(self):
        self.adj_list = {}
        self.people = {}

    def add_vertex(self, person):
        self.people[person.name] = person
        if person.name not in self.adj_list:
            self.adj_list[person.name] = []

    def add_edge(self, from_person, to_person):
        if from_person in self.adj_list:
            self.adj_list[from_person].append(to_person)

    def list_following(self, person):
        return self.adj_list.get(person, [])

    def list_followers(self, person):
        return [p for p, follows in self.adj_list.items() if person in follows]

    def view_profile(self, person):
        p = self.people.get(person)
        if p:
            print(f"Name: {p.name}")
            if p.is_public:
                print(f"Gender: {p.gender}\nBio: {p.bio}")
            else:
                print("Private profile.")

    def menu(self):
        while True:
            print("\nMenu:\n1. List Users\n2. View Profile\n3. View Following\n4. View Followers\n5. Exit")
            choice = input("Choose: ")
            if choice == '1':
                for name in self.people:
                    print(name)
            elif choice == '2':
                name = input("Enter username: ")
                self.view_profile(name)
            elif choice == '3':
                name = input("Enter username: ")
                print("Following:", self.list_following(name))
            elif choice == '4':
                name = input("Enter username: ")
                print("Followers:", self.list_followers(name))
            elif choice == '5':
                break

# Setup for Graph
users = [
    Person("Alice", "Female", "Likes books", True),
    Person("Bob", "Male", "Loves coding", False),
    Person("Charlie", "Male", "Traveler", True),
    Person("Diana", "Female", "Photographer", True),
    Person("Eve", "Female", "Gamer", False)
]
graph = UDGraph()
for user in users:
    graph.add_vertex(user)

graph.add_edge("Alice", "Bob")
graph.add_edge("Bob", "Alice")
graph.add_edge("Charlie", "Diana")
graph.add_edge("Eve", "Alice")

# Uncomment to run:
# graph.menu()