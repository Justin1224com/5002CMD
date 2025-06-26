import threading
import time

def generate_numbers():
    return [random.randint(0, 10000) for _ in range(100)]

def run_threads():
    results = []
    for _ in range(10):
        start = time.time_ns()
        threads = []
        for _ in range(3):
            t = threading.Thread(target=generate_numbers)
            threads.append(t)
            t.start()
        for t in threads:
            t.join()
        end = time.time_ns()
        duration = end - start
        results.append(duration)
        print(f"Round: Time taken = {duration} ns")
    avg = sum(results) / 10
    print(f"Average time (with threading): {avg:.2f} ns")

def run_no_threads():
    results = []
    for _ in range(10):
        start = time.time_ns()
        for _ in range(3):
            generate_numbers()
        end = time.time_ns()
        duration = end - start
        results.append(duration)
        print(f"Round: Time taken = {duration} ns")
    avg = sum(results) / 10
    print(f"Average time (no threading): {avg:.2f} ns")

# Uncomment to run:
# run_threads()
# run_no_threads()
