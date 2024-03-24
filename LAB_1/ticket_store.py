from datetime import datetime
import time
from threading import Semaphore, Thread

# Initial timestamp for calculating elapsed seconds
INITIAL_TIMESTAMP = datetime.now()

def get_elapsed_seconds() -> float:
    return round((datetime.now() - INITIAL_TIMESTAMP).total_seconds(), 1)

class Store:
    def __init__(self, max_occupancy):
        self.earnings = 0
        self.max_occupancy = Semaphore(max_occupancy)
        self.earnings_semaphore = Semaphore(1)

    def enter_store(self, customer):
        # Critical section: entering the store
        self.max_occupancy.acquire()
        print(f"{get_elapsed_seconds()}s: {customer['name']} (entering)")

    def leave_store(self, customer, ticket_price):
        # Critical section: leaving the store
        with self.earnings_semaphore:
            self.earnings += customer["ticketCount"] * ticket_price
            self.max_occupancy.release()

        print(f"{get_elapsed_seconds()}s: {customer['name']} (leaving)")

def customer_behavior(customer, store, ticket_price):
    time.sleep(customer["joinDelay"])
    store.enter_store(customer)
    time.sleep(customer["timeInStore"])
    store.leave_store(customer, ticket_price)

def simulate_store(customers: [dict], ticket_price: float, max_occupancy: int, n_vips: int) -> float:
    store = Store(max_occupancy)
    threads = []

    # Start threads for each customer
    for customer in customers:
        thread = Thread(target=customer_behavior, args=(customer, store, ticket_price), name=customer["name"])
        threads.append(thread)
        thread.start()

    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    return store.earnings


