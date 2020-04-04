import numpy as np

covered_rows = []
covered_columns = []
altered_expense_matrix = np.array([])
starred_zeros = []
primed_zeros = []


def get_assignments(expense_matrix):

    initialize_global_variables()
    global altered_expense_matrix
    altered_expense_matrix = np.array(expense_matrix[::])

    preliminaries()
    while have_uncovered_zeros():
        uncovered_zeros_handling()
    while len(covered_columns) != expense_matrix.shape[1]:
        subtract_and_add_minimal_uncovered_element()
        while have_uncovered_zeros():
            uncovered_zeros_handling()
    assignments = starred_zeros[::]
    delete_global_variables()
    return assignments


def preliminaries():
    subtract_row_minimum()
    subtract_columns_minimum()
    star_alone_zeros_and_cover_their_columns()
    return


def subtract_row_minimum():
    global altered_expense_matrix

    for row in range(altered_expense_matrix.shape[1]):
        minimum = np.min(altered_expense_matrix[row, :])
        altered_expense_matrix[row, :] = altered_expense_matrix[row, :] - minimum


def subtract_columns_minimum():
    global altered_expense_matrix

    for column in range(altered_expense_matrix.shape[1]):
        minimum = np.min(altered_expense_matrix[:, column])
        altered_expense_matrix[:, column] = altered_expense_matrix[:, column] - minimum


def star_alone_zeros_and_cover_their_columns():
    global altered_expense_matrix, covered_columns, starred_zeros

    column_with_zeros = []
    for row_num in range(altered_expense_matrix.shape[1]):
        for column_num in np.delete(range(len(altered_expense_matrix)), column_with_zeros):
            if altered_expense_matrix[row_num, column_num] == 0:
                column_with_zeros.append(column_num)
                if is_the_only_zero_in_row_and_column(row_num, column_num):
                    covered_columns.append(column_num)
                    starred_zeros.extend([[row_num, column_num]])
                break


def is_the_only_zero_in_row_and_column(row_num, column_num):
    row_to_check = altered_expense_matrix[row_num, :]
    column_to_check = altered_expense_matrix[:, column_num]
    return np.count_nonzero(row_to_check == 0) == 1 and np.count_nonzero(column_to_check == 0) == 1


def uncovered_zeros_handling():
    global covered_columns, covered_rows, primed_zeros

    go_to_step_2 = False
    for row_num in np.delete(range(altered_expense_matrix.shape[1]), covered_rows):
        for column_num in np.delete(range((altered_expense_matrix.shape[1])), covered_columns):
            if altered_expense_matrix[row_num, column_num] == 0:
                primed_zeros.extend([[row_num, column_num]])
                starred_zero_in_row = find_starred_zero_in_row_if_any(row_num)
                if starred_zero_in_row:
                    covered_columns.remove(starred_zero_in_row[1])
                    covered_rows.append(row_num)
                else:
                    go_to_step_2 = True
                break
        if go_to_step_2:
            break
    if go_to_step_2:
        alternating_starred_and_primed_zeros()


def find_starred_zero_in_row_if_any(row_num):
    for starred_zero in starred_zeros:
        if starred_zero[0] == row_num:
            return starred_zero
    return []


def alternating_starred_and_primed_zeros():
    uncovered_primed_zero = primed_zeros[-1]
    primed_zeros_in_sequence = [uncovered_primed_zero]
    starred_zeros_in_sequence = []
    starred_zero = find_starred_zero_in_column_if_any(primed_zeros_in_sequence[-1])
    while starred_zero:
        starred_zeros_in_sequence.extend([starred_zero])
        new_primed_zero_in_sequence = find_primed_zero_in_row(starred_zero)
        primed_zeros_in_sequence.extend([new_primed_zero_in_sequence])
        starred_zero = find_starred_zero_in_column_if_any(new_primed_zero_in_sequence)
    un_star_every_starred_star_every_primed_in_sequence(starred_zeros_in_sequence, primed_zeros_in_sequence)
    erase_primes_uncover_rows_and_cover_columns_with_starred_zeros()


def find_starred_zero_in_column_if_any(primed_zero):
    column_num = primed_zero[1]
    for starred_zero in starred_zeros:
        if starred_zero[1] == column_num:
            return starred_zero
    return []


def find_primed_zero_in_row(starred_zero):
    row_num = starred_zero[0]
    for primed_zero in primed_zeros:
        if primed_zero[0] == row_num:
            return primed_zero
    raise ValueError('must be primed zero in starred zero row')


def un_star_every_starred_star_every_primed_in_sequence(starred_in_sequence, primed_in_sequence):
    global starred_zeros, primed_zeros

    for starred_zero in starred_in_sequence:
        starred_zeros.remove(starred_zero)

    for primed_zero in primed_in_sequence:
        starred_zeros.extend([primed_zero])


def erase_primes_uncover_rows_and_cover_columns_with_starred_zeros():
    global covered_rows, covered_columns, primed_zeros

    primed_zeros = []
    covered_rows = []
    for starred_zero in starred_zeros:
        if starred_zero[1] not in covered_columns:
            covered_columns.append(starred_zero[1])


def have_uncovered_zeros():
    uncovered_sub_matrix = np.delete(np.delete(altered_expense_matrix, covered_rows, axis=0), covered_columns, axis=1)
    return 0 in uncovered_sub_matrix


def subtract_and_add_minimal_uncovered_element():
    global altered_expense_matrix

    uncovered_sub_matrix = np.delete(np.delete(altered_expense_matrix, covered_rows, axis=0), covered_columns, axis=1)
    minimum_value = np.min(uncovered_sub_matrix)

    for covered_row in covered_rows:
        altered_expense_matrix[covered_row, :] = np.add(altered_expense_matrix[covered_row, :], minimum_value)

    for uncovered_column in np.delete(range(altered_expense_matrix.shape[1]), covered_columns):
        altered_expense_matrix[:, uncovered_column] = np.subtract(altered_expense_matrix[:, uncovered_column],
                                                                  minimum_value)


def compute_total_expense(expense_matrix, assignments):
    total_expense = 0
    for assignment in assignments:
        total_expense += expense_matrix[assignment[0], assignment[1]]
    return total_expense


def initialize_global_variables():
    global covered_rows, covered_columns, altered_expense_matrix, starred_zeros, primed_zeros
    covered_rows = []
    covered_columns = []
    altered_expense_matrix = np.array([])
    starred_zeros = []
    primed_zeros = []


def delete_global_variables():
    global covered_rows, covered_columns, altered_expense_matrix, starred_zeros, primed_zeros
    del covered_rows, covered_columns, altered_expense_matrix, starred_zeros, primed_zeros
