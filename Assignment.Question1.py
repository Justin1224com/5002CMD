# ================================
# Question 1: Hashing
# ================================
import random
import time

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, ic_number):
        ic_str = str(ic_number)
        folded = sum(int(ic_str[i:i+4]) for i in range(0, len(ic_str), 4))
        return folded % self.size

    def insert(self, ic_number):
        index = self.hash_function(ic_number)
        if ic_number not in self.table[index]:
            self.table[index].append(ic_number)
            return len(self.table[index]) - 1  # collisions = size - 1
        return 0  # no collision

def generate_ic():
    return ''.join(str(random.randint(0, 9)) for _ in range(12))

def simulate_hashing():
    sizes = [1009, 2003]
    for size in sizes:
        print(f"\nHash Table Size: {size}")
        total_collisions = []
        for round_num in range(10):
            table = HashTable(size)
            round_collisions = 0
            for _ in range(1000):
                ic = generate_ic()
                round_collisions += table.insert(ic)
            total_collisions.append(round_collisions)
            print(f"Round {round_num+1} Collisions: {round_collisions}")
        avg = sum(total_collisions) / 10
        print(f"Average Collisions: {avg:.2f}")