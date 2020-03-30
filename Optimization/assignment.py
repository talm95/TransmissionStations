import numpy as np


def assign_matrix(expense_matrix):

    altered_expense_matrix = np.array(expense_matrix[::])

    subtract_rows_minimum(altered_expense_matrix)

    subtract_columns_minimum(altered_expense_matrix)

    assignments, lined_rows, lined_columns = find_best_assignments(altered_expense_matrix)
    while len(assignments) < expense_matrix.shape[1]:
        subtract_minimum_from_uncrossed_elements_add_to_intersections(altered_expense_matrix, lined_rows, lined_columns)

        subtract_rows_minimum(altered_expense_matrix)

        subtract_columns_minimum(altered_expense_matrix)

        assignments, lined_rows, lined_columns = find_best_assignments(altered_expense_matrix)

    return assignments


def find_best_assignments(altered_expense_matrix):
    lined_rows = []
    lined_columns = []
    assignments = []

    found_no_new_assignments = 0

    while 0 in np.delete(np.delete(altered_expense_matrix, lined_rows, axis=0), lined_columns, axis=1):

        while found_no_new_assignments < 2 and 0 in np.delete(np.delete(altered_expense_matrix, lined_rows, axis=0),
                                                              lined_columns, axis=1):
            new_assignments = find_rows_with_only_one_zero(altered_expense_matrix, lined_rows, lined_columns)
            assignments.extend(new_assignments)
            found_no_new_assignments = 0 if len(new_assignments) > 0 else found_no_new_assignments + 1

            if found_no_new_assignments > 1 or 0 not in np.delete(np.delete(altered_expense_matrix, lined_rows, axis=0),
                                                                  lined_columns, axis=1):
                break
            
            new_assignments = find_columns_with_only_one_zero(altered_expense_matrix, lined_rows, lined_columns)
            assignments.extend(new_assignments)
            found_no_new_assignments = 0 if len(new_assignments) > 0 else found_no_new_assignments + 1

        if 0 in np.delete(np.delete(altered_expense_matrix, lined_rows, axis=0), lined_columns, axis=1):
            new_assignments = solve_multiple_solutions_situation(altered_expense_matrix, lined_rows, lined_columns)
            assignments.extend(new_assignments)
            found_no_new_assignments = 0

    return assignments, lined_rows, lined_columns


def find_rows_with_only_one_zero(altered_expense_matrix, lined_rows, lined_columns):
    assignments = []
    unlined_rows = np.delete(range(altered_expense_matrix.shape[1]), lined_rows)
    for row_num in unlined_rows:
        num_of_zeros_in_row = 0
        assignment = []
        column_to_line = []
        for column_num in np.delete(range(altered_expense_matrix.shape[1]), lined_columns):
            if altered_expense_matrix[row_num][column_num] == 0:
                num_of_zeros_in_row += 1
                assignment = [[row_num, column_num]]
                column_to_line = column_num
                if num_of_zeros_in_row > 1:
                    break
        if num_of_zeros_in_row == 1:
            assignments.extend(assignment)
            lined_columns.append(column_to_line)

    return assignments


def find_columns_with_only_one_zero(altered_expense_matrix, lined_rows, lined_columns):
    reversed_assignments = find_rows_with_only_one_zero(np.transpose(altered_expense_matrix), lined_columns, lined_rows)
    assignments = []
    for reversed_assignment in reversed_assignments:
        assignments.extend([reversed_assignment[::-1]])
    return assignments


def solve_multiple_solutions_situation(altered_expense_matrix, lined_rows, lined_columns):
    new_assignment = find_first_zero_in_uncrossed_lines(altered_expense_matrix, lined_rows, lined_columns)
    temporarily_lined_row = new_assignment[0]
    temporarily_lined_column = new_assignment[1]
    lined_rows.append(temporarily_lined_row)
    lined_columns.append(temporarily_lined_column)

    new_assignments = find_rows_with_only_one_zero(altered_expense_matrix, lined_rows, lined_columns)
    if len(new_assignments) > 0:
        new_assignments.extend([new_assignment])
        return new_assignments
    else:
        new_assignments = find_columns_with_only_one_zero(altered_expense_matrix, lined_rows, lined_columns)
        new_assignments.extend([new_assignment])
        return new_assignments


def find_first_zero_in_uncrossed_lines(altered_expense_matrix, lined_rows, lined_columns):
    for row_num in np.delete(range(altered_expense_matrix.shape[1]), lined_rows):
        for column_num in np.delete(range(altered_expense_matrix.shape[1]), lined_columns):
            if altered_expense_matrix[row_num][column_num] == 0:
                return [row_num, column_num]


def subtract_rows_minimum(altered_expense_matrix):
    for row in range(altered_expense_matrix.shape[1]):
        minimum = np.min(altered_expense_matrix[row, :])
        altered_expense_matrix[row, :] = altered_expense_matrix[row, :] - minimum


def subtract_columns_minimum(altered_expense_matrix):
    for column in range(altered_expense_matrix.shape[1]):
        minimum = np.min(altered_expense_matrix[:, column])
        altered_expense_matrix[:, column] = altered_expense_matrix[:, column] - minimum


def subtract_minimum_from_uncrossed_elements_add_to_intersections(altered_expense_matrix, lined_rows, lined_columns):
    intersections = []
    for lined_row in lined_rows:
        for lined_column in lined_columns:
            intersections.extend([[lined_row, lined_column]])

    sub_uncrossed_matrix = np.delete(np.delete(altered_expense_matrix, lined_rows, axis=0), lined_columns, axis=1)
    minimum = np.min(sub_uncrossed_matrix)
    for row_num in np.delete(range(altered_expense_matrix.shape[1]), lined_rows):
        for column_num in np.delete(range(altered_expense_matrix.shape[1]), lined_columns):
            altered_expense_matrix[row_num][column_num] -= minimum

    for intersection in intersections:
        altered_expense_matrix[intersection[0]][intersection[1]] += minimum


def compute_assignment_total_expense(expense_matrix, assignments):
    total_expense = 0
    for assignment in assignments:
        total_expense += expense_matrix[assignment[0]][assignment[1]]
    return total_expense
