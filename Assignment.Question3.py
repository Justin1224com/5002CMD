import threading
import time
import random
from multiprocessing import Process


# Generate 100 random numbers
def generate_numbers():
    return [random.randint(0, 10000) for _ in range(10000)]

# Multithreaded execution
def run_with_threads(rounds=10):
    results = []

    def task(start_times, end_times, index):
        start_times[index] = time.time_ns()
        generate_numbers()
        end_times[index] = time.time_ns()

    for _ in range(rounds):
        start_times = [0] * 3
        end_times = [0] * 3
        threads = []

        # Start all 3 threads
        for i in range(3):
            t = threading.Thread(target=task, args=(start_times, end_times, i))
            threads.append(t)
            t.start()

        # Wait for all threads to finish
        for t in threads:
            t.join()

        # Calculate time as t2 - t1
        t1 = min(start_times)
        t2 = max(end_times)
        results.append(t2 - t1)

    return results

# Single-threaded execution
def run_without_threads(rounds=10):
    times = []
    for _ in range(rounds):
        start = time.time_ns()
        for _ in range(3):
            generate_numbers()
        end = time.time_ns()
        times.append(end - start)
    return times

# Main comparison logic
multi_times = run_with_threads()
no_thread_times = run_without_threads()

print("\nRound-by-Round Performance Comparison:")
print("--------------------------------------------------------------------------------------")
print("| Round | Multithreading Time (ns) | Non-Multithreading Time (ns) | Difference (ns) |")
print("--------------------------------------------------------------------------------------")

for i in range(10):
    m = multi_times[i]
    n = no_thread_times[i]
    diff = n - m
    print(f"| {i+1:^5} | {m:^25} | {n:^29} | {diff:^16} |")

print("--------------------------------------------------------------------------------------")

# Summary of results
total_m = sum(multi_times)
total_n = sum(no_thread_times)
avg_m = total_m / 10
avg_n = total_n / 10
diff_total = total_n - total_m
diff_avg = avg_n - avg_m

print("\nSummary of Results:")
print("--------------------------------------------------------------------------")
print("| Metric         | Multithreading (ns) | Non-Multithreading (ns) | Difference (ns) |")
print("--------------------------------------------------------------------------")
print(f"| Total Time     | {total_m:^21} | {total_n:^23} | {diff_total:^15} |")
print(f"| Average Time   | {avg_m:^21.1f} | {avg_n:^23.1f} | {diff_avg:^15.1f} |")
print("--------------------------------------------------------------------------")
