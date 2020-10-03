import copy

class Game:
    def __init__(self, field):
            self.step = 0
            self.cur_field = copy.deepcopy(field)
            self.tmp_field = []
            for r in range(len(field)):
                self.tmp_field.append([])
                for e in range(len(field[0])):
                    self.tmp_field[r].append(0)

    def next_step(self):
        zero_field = copy.deepcopy(self.tmp_field)
        for i in range(len(self.cur_field)):
            for j in range(len(self.cur_field[0])):
                self.tmp_field[i][j] = game.next_value(self.cur_field, i , j)
        self.cur_field = self.tmp_field
        self.tmp_field = zero_field
        pass

    @staticmethod
    def next_value(field, i, j):
        num_rows = len(field)
        num_colums = len(field[0])
        sum = field[(i + num_rows - 1) % num_rows][(j + num_colums - 1) % num_colums]
        sum += field[(i + num_rows - 1) % num_rows][j]
        sum += field[(i + num_rows - 1) % num_rows][(j + 1) % num_colums]
        sum += field[i][(j + num_colums - 1) % num_colums]
        sum += field[i][(j + 1) % num_colums]
        sum += field[(i + 1) % num_rows][(j + num_colums - 1) % num_colums]
        sum += field[(i + 1) % num_rows][j]
        sum += field[(i + 1) % num_rows][(j + 1) % num_colums]

        rv = 0
        if field[i][j] == 0 and sum == 3:
            rv = 1
        elif field[i][j] == 1 and (sum == 2 or sum == 3):
            rv = 1
        return rv

    def print_tmp_field(self):
        for e in self.tmp_field:
            print(*e)


    def print_field(self):
        for e in self.cur_field:
            print(*e)

if __name__ == '__main__':
    dflt_field = [[0, 0, 1, 0, 0, 0],
                  [1, 0, 1, 0, 0, 0],
                  [0, 1, 1, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0]]
    game = Game(dflt_field)
    print("START GAME")
    while True:
        game.print_field()
        game.next_step()
        print("")