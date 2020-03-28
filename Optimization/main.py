from Utils.Objects import *
from Utils.clients_serving_expense import initialize_expense_matrix
from Utils.imaging import draw_map_before_assigning
from assignment import assign_clients_to_stations
from assignment import compute_assignment_total_expense

map_size = 10
number_of_stations = 3
number_of_clients = 10
max_clients_per_station = 2

stations = randomize_stations(map_size, number_of_stations)
clients = randomize_clients(map_size, number_of_clients)

expense_matrix = initialize_expense_matrix(stations, clients, max_clients_per_station)

print "the expense matrix is:"
print expense_matrix

assignments = assign_clients_to_stations(expense_matrix)
print "the assignments are:"
print assignments

total_expense = compute_assignment_total_expense(expense_matrix, assignments)
print "the total expense is:"
print total_expense

# draw_map_before_assignment

# draw_map_before_assigning(map_size, stations, clients)

# assign

# draw map after assigning

# print stations
# print clients
# print expense_matrix
