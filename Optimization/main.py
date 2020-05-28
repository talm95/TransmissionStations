from Utils.Objects import *
from Utils.clients_serving_expense import initialize_expense_matrix
from Utils.imaging import draw_map_of_assignments
from hungarian_algorithm import get_assignments
from hungarian_algorithm import compute_total_expense
import time

map_size = 20
number_of_stations = 3
number_of_clients = 3
max_clients_per_station = 1

stations = randomize_stations(map_size, number_of_stations)
clients = randomize_clients(map_size, number_of_clients)

expense_matrix = initialize_expense_matrix(stations, clients, max_clients_per_station)

initial_time = time.clock()
assignments = get_assignments(expense_matrix)
solve_time = time.clock() - initial_time
print ('total time is ' + str(solve_time))

total_expense = compute_total_expense(expense_matrix, assignments)
print "the total expense is:"
print total_expense

assign_clients_to_stations(assignments, clients, number_of_stations, max_clients_per_station)

draw_map_of_assignments(map_size, stations, clients)
