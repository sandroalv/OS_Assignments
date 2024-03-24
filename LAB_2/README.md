# Distributed Shopping List

**Introduction**
This project implements a simple yet effective shopping list application following the client-server model using Python. The application facilitates managing a shopping list through a client interface that communicates with a server holding the shopping list data. This model demonstrates the basics of API communication, client-server interaction, and handling concurrent client requests using sockets.

**Server Application:**
Maintains the shopping list data.
Supports two primary actions: retrieving all items and adding a new item to the shopping list.
Creates a backup of the shopping list upon receiving a SIGTERM signal.
Properly closes connections and shuts down on receiving a CTRL + C command.
Queues up to 5 concurrent connection requests.
Runs indefinitely until manually terminated.

**Client Application:**
Provides a user-friendly console interface for interacting with the shopping list.
Allows users to add a new item or retrieve the list of items.
Communicates with the server application using sockets.
Runs in a loop, offering a menu of actions until the user decides to exit.

**Communication Protocol**
The client and server applications use a custom communication protocol over sockets. For every client request, the server responds appropriately, ensuring a seamless exchange of information. The protocol supports adding items to the list and retrieving the current list of items.

**Requirements**
Independent and non-nested processes for server and client(s).
Communication between server and client(s) via sockets.
The server can queue up to 5 connection requests.
The server and client(s) offer robust error handling and clean shutdown processes.
Implementations adhere to the communication protocol outlined above.

To run the server application:
python server.py

To run the client application in a separate terminal:
python client.py
