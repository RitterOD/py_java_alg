from random import *

class TortoiseTask:
    def __init__(self, row_amnt, col_amnt, min_price, max_price):
        self.row_amnt = row_amnt
        self.col_amnt = col_amnt
        self.min_price = min_price
        self.max_price = max_price
        self.field = None
        self.solve_field = None

    def generate_field(self):
        field = []
        for row_ind in range(self.row_amnt):
            field.append([0] * self.col_amnt)
        for row_ind in range(len(field)):
            for col_ind in range(len(field[row_ind])):
                field[row_ind][col_ind] = randint(self.min_price, self.max_price)
        self.field = field

    def get_field(self):
        return self.field

    def get_solve_field(self):
        return self.solve_field

    def solve(self):
        solve_field = []
        for row_ind in range(self.row_amnt):
            solve_field.append([0] * self.col_amnt)
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
        self.solve_field = solve_field
        return solve_field[self.row_amnt - 1][self.col_amnt - 1]

    def getWay(self):
        cur_row = self.row_amnt - 1
        cur_col = self.col_amnt - 1
        cur_sum = self.solve_field[cur_row][cur_col]
        way = [(cur_row, cur_col)]
        while cur_row != 0 or cur_col != 0:
            next_sum = cur_sum - self.field[cur_row][cur_col]
            if (next_sum == self.solve_field[cur_row - 1][cur_col] and
                    cur_row - 1 >= 0):
                cur_row -= 1
            elif (next_sum == self.solve_field[cur_row][cur_col - 1] and
                    cur_col - 1 >= 0):
                cur_col -= 1
            cur_sum = next_sum
            way.append((cur_row, cur_col))
        way.reverse()
        return way


if __name__ == "__main__":
    tortoiseTask = TortoiseTask(5, 10, 1, 9)
    tortoiseTask.generate_field()
    field = tortoiseTask.get_field()
    print("field\n")
    for row in field:
        print(row)
    print("end field")
    rv = tortoiseTask.solve()
    print("\nsolution =", rv, "\n")
    rv = tortoiseTask.getWay()
    solve_field = tortoiseTask.get_solve_field()
    print("solve field")
    for row in solve_field:
        print(row)
    print("end solve field\n")
    print("Way =", rv)
