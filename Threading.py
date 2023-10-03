from time import sleep, time
import threading

start_time = time()
def example(id):
    print(f"Going to sleep... {id}")
    sleep(1)
    print(f"Woken up... {id}")

end_time = time()

threads = [threading.Thread(target=example, args=[i]) for i in range(3)]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

# t1 = threading.Thread(target=example, args=[1])
# t2 = threading.Thread(target=example, args=[2])

# t1.start()
# t2.start()

# t1.join()
# t2.join()

print(f"Start Time : {start_time}")
print(f"End Time : {end_time}")
print(f"Main Thread Ending : {end_time - start_time}")
