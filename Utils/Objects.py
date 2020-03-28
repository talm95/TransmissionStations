import random


def randomize_stations(map_size, number_of_stations):
    stations = []
    for i in range(number_of_stations):
        stations.append([random.uniform(0, map_size), random.uniform(0, map_size)])
    return stations


def randomize_clients(map_size, number_of_clients):
    clients = []
    for i in range(number_of_clients):
        client_pos = [random.uniform(0, map_size), random.uniform(0, map_size)]
        client_priority = random.randint(1, 3)
        client = {"client_pos": client_pos,
                  "client_priority": client_priority}
        clients.append(client)
    return clients


def filter_clients_by_priority(clients, priority):
    filtered_clients = filter(lambda client: client.get("client_priority") == priority, clients)
    return filtered_clients


def get_clients_filtered_by_priority(clients):
    first_priority_clients = filter_clients_by_priority(clients, 1)
    second_priority_clients = filter_clients_by_priority(clients, 2)
    third_priority_clients = filter_clients_by_priority(clients, 3)
    return first_priority_clients, second_priority_clients, third_priority_clients


def get_clients_pos(clients):
    clients_pos = []
    for client in clients:
        clients_pos.append(client.get("client_pos"))
    return clients_pos
