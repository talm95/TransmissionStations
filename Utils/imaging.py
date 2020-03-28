import matplotlib.pyplot as plt
from Utils.Objects import get_clients_filtered_by_priority
from Utils.Objects import get_clients_pos


def draw_map_before_assigning(map_size, stations, clients):
    fig, ax = plt.subplots(1, 1)
    ax.scatter(*zip(*stations), marker='^', color='k', label='Stations')

    first_priority_clients, second_priority_clients, third_priority_clients = get_clients_filtered_by_priority(clients)
    if len(first_priority_clients) > 0:
        ax.scatter(*zip(*get_clients_pos(first_priority_clients)), marker='.', color='r', label='First priority clients')

    if len(second_priority_clients) > 0:
        ax.scatter(*zip(*get_clients_pos(second_priority_clients)), marker='.', color='b', label='Second priority clients')

    if len(third_priority_clients) > 0:
        ax.scatter(*zip(*get_clients_pos(third_priority_clients)), marker='.', color='g', label='Third priority clients')

    ax.set_title('Stations and clients before assignment')
    ax.set_xlim(0, map_size + map_size/5)
    ax.set_ylim(0, map_size + map_size/5)
    leg = ax.legend()
    plt.show()
