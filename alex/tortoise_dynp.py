from random import *

class TortoiseTask:
    def __init__(self, n, m, min_price, max_price):
        self.n = n
        self.m = m
        self.min_price = min_price
        self.max_price = max_price
        self.field = None
        self.solve_filed = None

    def generate_field(self):
        field = []
        for row_ind in range(self.n):
            field.append([0] * self.m)
        for row_ind in range(len(field)):
            for col_ind in range(len(field[row_ind])):
                field[row_ind][col_ind] = randint(self.min_price, self.max_price)
        self.field = field

    def getField(self):
        return self.field

    def solve(self):
        solve_field = []
        for row_ind in range(self.n):
            solve_field.append([0] * self.m)
        solve_field[0][0] = self.field[0][0]
        for col_num in range(1, len(self.field[0])):
            solve_field[0][col_num] = solve_field[0][col_num - 1] + self.field[0][col_num]
        for row_num in range(1, len(self.field)):
            solve_field[row_num][0] = solve_field[row_num - 1][0] + self.field[row_num][0]
        for col_num in range(1, len(self.field[0])):
            for row_num in range(1, len(self.field)):
                first_val = solve_field[row_num - 1][col_num] + self.field[row_num][col_num]
                second_val = solve_field[row_num][col_num - 1] + self.field[row_num][col_num]
                if first_val > second_val:
                    solve_field[row_num][col_num] = first_val
                else:
                    solve_field[row_num][col_num] = second_val
        print("solve field\n")
        for row in solve_field:
            print(row)
        print("end solve field\n")
        self.solve_filed = solve_field
        return solve_field[self.n - 1][self.m - 1]

if __name__ == "__main__":
    tortoiseTask = TortoiseTask(3, 3, 1, 9)
    tortoiseTask.generate_field()
    field = tortoiseTask.getField()
    for row in field:
        print(row)
    rv = tortoiseTask.solve()

    print("solution =", rv)