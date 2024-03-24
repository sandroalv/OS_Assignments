# Virtual Ticket Store Simulation

**Introduction**
In the digital age, buying tickets for events often involves waiting in virtual queues. This project simulates a virtual store where customers wait in line to purchase tickets for events like concerts or football games. The simulation models customer behavior as they join the queue, wait their turn, and make their purchases, all managed through a Python-based system.

**Scenario**
The simulation operates with two primary files: main.py and ticket_store.py. While main.py sets the simulation parameters and initiates the process, ticket_store.py contains the core logic for customer management and store operations. The simulation also utilizes a JSON file, customers.json, to input customer data, including names, ticket requirements, and VIP status.

Customers are differentiated by their VIP status, with VIPs receiving priority access to the store. However, in this implementation, the queue is solely based on join delay, ensuring a first-come, first-served basis regardless of VIP status.

**Implementation**
The project's main challenge lies in correctly synchronizing customer threads to reflect real-world scenarios of a virtual queue. Each customer's actions—joining the store, spending time within, and purchasing tickets—are represented through thread operations. Synchronization mechanisms ensure that the store does not exceed its maximum occupancy and that VIP customers are prioritized according to the initial project requirements.

To run the simulation, users specify the ticket price and maximum store occupancy as command-line arguments, allowing for dynamic simulation scenarios.

**Features**
Simulation of customer behavior in a virtual queue.
Dynamic simulation parameters through command-line arguments.
Synchronization of customer threads to manage store occupancy effectively.
This project offers a simplified yet insightful look into the complexities of managing virtual queues for high-demand events, providing a foundational understanding of thread synchronization and customer priority management in software systems.

