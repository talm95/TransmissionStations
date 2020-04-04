from unittest import TestCase
from hungarian_algorithm import get_assignments
from hungarian_algorithm import compute_total_expense
import numpy as np


class TestAssignment(TestCase):
    def test_assignment_1(self):
        expense_matrix = np.array([[1, 2, 3, 4],
                                   [1, 2, 3, 4],
                                   [1, 2, 3, 4],
                                   [1, 2, 3, 4]])
        assignments = get_assignments(expense_matrix)
        total_expense = compute_total_expense(expense_matrix, assignments)
        self.assertEquals(total_expense, 10)

    def test_assignment_2(self):
        expense_matrix = np.array([[1, 2, 2, 2],
                                   [2, 1, 2, 2],
                                   [2, 2, 1, 2],
                                   [2, 2, 2, 1]])
        assignments = get_assignments(expense_matrix)
        total_expense = compute_total_expense(expense_matrix, assignments)
        self.assertEquals(total_expense, 4)

    def test_assignment_3(self):
        expense_matrix = np.array([[5, 3, 2, 8],
                                   [7, 9, 2, 6],
                                   [6, 4, 5, 7],
                                   [5, 7, 7, 8]])
        assignments = get_assignments(expense_matrix)
        total_expense = compute_total_expense(expense_matrix, assignments)
        self.assertEquals(total_expense, 17)

    def test_assignment_4(self):
        expense_matrix = np.array([[28.64862278, 28.64862278, 10.7553251, 10.7553251, 14.48204193, 14.48204193,
                                    0., 0., 0., 0.],
                                   [10.37246688, 10.37246688, 2.52115728, 2.52115728, 0.79582408, 0.79582408,
                                    0., 0., 0., 0.],
                                   [5.9629539, 5.9629539, 2.84379799, 2.84379799, 2.37244864, 2.37244864,
                                    0., 0., 0., 0.],
                                   [8.71566682, 8.71566682, 12.75535525, 12.75535525, 9.32306079, 9.32306079,
                                    0., 0., 0., 0.],
                                   [3.65731128, 3.65731128, 9.01342674, 9.01342674, 6.0167444, 6.0167444,
                                    0., 0., 0., 0.],
                                   [13.60745654, 13.60745654, 0.96887223, 0.96887223, 4.12784762, 4.12784762,
                                    0., 0., 0., 0.],
                                   [14.1549017, 14.1549017, 5.67157008, 5.67157008, 6.0038367, 6.0038367,
                                    0., 0., 0., 0.],
                                   [10.09629007, 10.09629007, 7.18409997, 7.18409997, 5.16929775, 5.16929775,
                                    0., 0., 0., 0.],
                                   [29.25588753, 29.25588753, 12.65687666, 12.65687666, 15.6494675, 15.6494675,
                                    0., 0., 0., 0.],
                                   [2.95464454, 2.95464454, 3.45413517, 3.45413517, 2.06763753, 2.06763753,
                                    0., 0., 0., 0.]])
        assignments = get_assignments(expense_matrix)
        total_expense = compute_total_expense(expense_matrix, assignments)
        self.assertTrue(no_more_than_one_assignment_per_row_and_column(assignments))
        self.assertEquals(total_expense, 16.38974787)


def no_more_than_one_assignment_per_row_and_column(assignments):
    rows_containing = []
    columns_containing = []
    for assignment in assignments:
        if assignment[0] in rows_containing or assignment[1] in columns_containing:
            return False
        rows_containing.append(assignment[0])
        columns_containing.append(assignment[1])
    return True
