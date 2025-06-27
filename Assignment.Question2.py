class UDGraph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, start, end):
        if start in self.graph and end in self.graph:
            self.graph[start].append(end)
        else:
            print("One or both vertices not found.")

    def list_outgoing_adjacent(self, vertex):
        return self.graph.get(vertex, [])

    def list_incoming_adjacent(self, vertex):
        return [v for v, edges in self.graph.items() if vertex in edges]

class Person:
    def __init__(self, name, privacy, bio):
        self.name = name
        self.privacy = privacy  # 'P' for private, 'U' for public
        self.bio = bio

    def get_name(self):
        return self.name

    def get_privacy(self):
        return self.privacy

    def get_bio(self):
        return self.bio

class SlowGram:
    def __init__(self):
        self.my_graph = UDGraph()
        self.people = {}

    def add_new_profile(self, name, privacy, bio):
        person = Person(name, privacy, bio)
        self.people[name] = person
        self.my_graph.add_vertex(name)
        return name

    def add_follow(self, follower, followee):
        self.my_graph.add_edge(follower, followee)

    def display_profiles(self):
        print("\n============================")
        print("View ALL Profile Names:")
        print("============================")
        for idx, name in enumerate(self.people, 1):
            print(f"{idx}.) {name}")

    def display_profile(self, index):
        person = list(self.people.values())[index - 1]
        print(f"Name: {person.get_name()}")
        if person.get_privacy() == 'U':
            print(f"Biography: {person.get_bio()}")
        else:
            print(f"{person.get_name()} has a private profile.")

    def view_followers(self, index):
        name = list(self.people.keys())[index - 1]
        followers = self.my_graph.list_incoming_adjacent(name)
        print("Follower List:")
        for f in followers:
            print(f"- {f}")

    def view_followings(self, index):
        name = list(self.people.keys())[index - 1]
        followings = self.my_graph.list_outgoing_adjacent(name)
        print("Following List:")
        for f in followings:
            print(f"- {f}")

    def menu(self):
        while True:
            print("\n***************************************")
            print("Welcome to Slow Gram, Your New Social Media App:")
            print("***************************************")
            print("1. View names of all profiles")
            print("2. View details for any profile")
            print("3. View followers of any profile")
            print("4. View followed accounts of any profile")
            print("5. Quit")

            choice = input("Enter your choice (1 - 5): ")
            if choice == '1':
                self.display_profiles()
            elif choice == '2':
                self.display_profiles()
                idx = int(input("Select whose profile to view (1 - 5): "))
                self.display_profile(idx)
            elif choice == '3':
                self.display_profiles()
                idx = int(input("Select whose profile to view followers (1 - 5): "))
                self.view_followers(idx)
            elif choice == '4':
                self.display_profiles()
                idx = int(input("Select whose profile to view followings (1 - 5): "))
                self.view_followings(idx)
            elif choice == '5':
                break

def main():
    gram = SlowGram()

    # Add profiles
    karen = gram.add_new_profile("Karen", "P", "Just an ordinary woman")
    susy = gram.add_new_profile("Susy", "U", "Just a normal person")
    brian = gram.add_new_profile("Brian", "U", "Just an ordinary teenager")
    calvin = gram.add_new_profile("Calvin", "P", "Just an ordinary man")
    elon = gram.add_new_profile("Elon", "P", "Just a hardworking man")

    # Add follow relationships
    gram.add_follow(karen, susy)
    gram.add_follow(karen, brian)
    gram.add_follow(karen, elon)
    gram.add_follow(elon, karen)
    gram.add_follow(elon, calvin)
    gram.add_follow(brian, karen)
    gram.add_follow(brian, susy)

    gram.menu()

main()
