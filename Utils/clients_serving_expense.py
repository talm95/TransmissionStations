import math
import numpy as np


def calculate_distance(pos1, pos2):
    distance = math.sqrt(math.pow(pos1[0] - pos2[0], 2) + math.pow(pos1[1] - pos2[1], 2))
    return distance


def calculate_client_serving_expense(station, client):
    distance = calculate_distance(station, client.get("client_pos"))
    serving_expense = distance*client.get("client_priority")
    return serving_expense


def initialize_expense_matrix(stations, clients, max_clients_per_station):
    expense_matrix = np.empty((len(clients), 0))
    for station in stations:
        expense_array = np.empty((0, 1))
        for client in clients:
            client_station_expense = calculate_client_serving_expense(station, client)
            expense_array = np.append(expense_array, np.array([[client_station_expense]]), axis=0)
        for i in range(max_clients_per_station):
            expense_matrix = np.append(expense_matrix, np.array(expense_array), axis=1)

    if are_too_many_clients(len(stations), len(clients), max_clients_per_station):
        zeros_array = np.zeros((len(clients), len(clients) - len(stations)*max_clients_per_station))
        expense_matrix = np.concatenate((expense_matrix, zeros_array), axis=1)

    return expense_matrix


def are_too_many_clients(number_of_stations, number_of_clients, max_clients_per_station):
    return number_of_clients > number_of_stations*max_clients_per_station
