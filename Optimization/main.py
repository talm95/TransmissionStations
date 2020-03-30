from Utils.Objects import *
from Utils.clients_serving_expense import initialize_expense_matrix
from Utils.imaging import draw_map_of_assignments
from assignment import assign_matrix
from assignment import compute_assignment_total_expense

map_size = 200
number_of_stations = 7
number_of_clients = 35
max_clients_per_station = 4

stations = randomize_stations(map_size, number_of_stations)
clients = randomize_clients(map_size, number_of_clients)

expense_matrix = initialize_expense_matrix(stations, clients, max_clients_per_station)

assignments = assign_matrix(expense_matrix)

total_expense = compute_assignment_total_expense(expense_matrix, assignments)
print "the total expense is:"
print total_expense

assign_clients_to_stations(assignments, clients, number_of_stations, max_clients_per_station)

draw_map_of_assignments(map_size, stations, clients)
