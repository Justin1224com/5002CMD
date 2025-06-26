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
        part1 = int(ic_number[0:4])
        part2 = int(ic_number[4:8])
        part3 = int(ic_number[8:12])
        folded = part1 + part2 + part3
        return folded % self.size
    def insert(self, ic_number):
        index = self.hash_function(ic_number)
        if ic_number not in self.table[index]:
            self.table[index].append(ic_number)
            return len(self.table[index]) - 1  # collisions = size - 1
        return 0  # no collision

def generate_ic():
    # YYMMDD
    year = random.randint(50, 99)
    month = random.randint(1, 12)
    day = random.randint(1, 28)  # Simplified for valid date
    dob = f"{year:02d}{month:02d}{day:02d}"

    # BP code (2 digits), from valid Malaysian codes
    bp_codes = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12',
                '13', '14', '15', '16', '21', '22', '23', '24', '25', '26', '27', '28',
                '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40',
                '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52',
                '53', '54', '55', '56', '57', '58', '59', '60', '61', '62', '63', '64',
                '65', '66', '67', '68', '69', '70', '71', '72', '74', '75', '76', '77',
                '78', '79', '82', '83', '84', '85', '86', '87', '88', '89', '90', '91',
                '92', '93', '98', '99']
    bp = random.choice(bp_codes)

    # Serial number + gender (###G)
    serial = random.randint(0, 999)
    gender = random.choice([0, 1])  # Even for female, odd for male
    g = random.randrange(0, 10, 2) if gender == 0 else random.randrange(1, 10, 2)
    end = f"{serial:03d}{g}"

    return f"{dob}{bp}{end}"

def simulate_hashing():
    sizes = [1009, 2003]
    table_names = ["Smaller", "Bigger"]
    average_collisions_list = []

    for idx, size in enumerate(sizes):
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
        average_collisions_list.append(avg)
        print(f"Average Collisions: {avg:.2f}")

    print()
    # Calculate and display collision rates
    for i in range(2):
        rate = (average_collisions_list[i] / 1000) * 100
        print(f"Collision Rate for {table_names[i]} Hash Table: {rate:.2f} %")


simulate_hashing()
