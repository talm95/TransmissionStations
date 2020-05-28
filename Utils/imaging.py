import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
from Utils.Objects import get_clients_filtered_by_priority
from Utils.Objects import get_clients_pos
from Utils.Objects import filter_clients_by_assigned_station


def draw_map_of_assignments(map_size, stations, clients):
    ax_before_assignment = plt.subplot(1, 2, 1)
    ax_before_assignment.scatter(*zip(*stations), marker='^', color='k', label='Stations')

    first_priority_clients, second_priority_clients, third_priority_clients = get_clients_filtered_by_priority(clients)
    if len(first_priority_clients) > 0:
        ax_before_assignment.scatter(*zip(*get_clients_pos(first_priority_clients)), marker='.', color='r',
                                     label='First priority clients')

    if len(second_priority_clients) > 0:
        ax_before_assignment.scatter(*zip(*get_clients_pos(second_priority_clients)), marker='.', color='b',
                                     label='Second priority clients')

    if len(third_priority_clients) > 0:
        ax_before_assignment.scatter(*zip(*get_clients_pos(third_priority_clients)), marker='.', color='g',
                                     label='Third priority clients')

    ax_before_assignment.set_title('Stations and clients before assignment')
    ax_before_assignment.set_xlim(-map_size/10, map_size + map_size/2)
    ax_before_assignment.set_ylim(-map_size/10, map_size + map_size/10)
    ax_before_assignment.legend()

    ax_after_assignment = plt.subplot(1, 2, 2)
    rainbow_map = cm.get_cmap('rainbow')
    stations_colors = [rainbow_map(i) for i in np.linspace(0, 1, len(stations))]
    for station_num in range(len(stations)):
        station = stations[station_num]
        ax_after_assignment.scatter(station[0], station[1], marker='^', color=stations_colors[station_num],
                                    label='station_number ' + str(station_num))
        this_station_assigned_clients = filter_clients_by_assigned_station(clients, station_num)
        if len(this_station_assigned_clients) > 0:
            ax_after_assignment.scatter(*zip(*get_clients_pos(this_station_assigned_clients)), marker='.',
                                        color=stations_colors[station_num])

    unassigned_clients = filter_clients_by_assigned_station(clients, -1)
    if len(unassigned_clients) > 0:
        ax_after_assignment.scatter(*zip(*get_clients_pos(unassigned_clients)), marker='.', color='k',
                                    label='unassigned_clients')

    ax_after_assignment.set_label('unassigned_clients')
    ax_after_assignment.set_title('Stations and clients after assignment')
    ax_after_assignment.set_xlim(-map_size/10, map_size + map_size / 2)
    ax_after_assignment.set_ylim(-map_size/10, map_size + map_size / 10)
    ax_after_assignment.legend()

    plt.show()
