
def calculate_structure(knapsack_weigt, way, weights):
    rv = [0] * len(weights)
    cur_column = knapsack_weigt
    cur_row = len(weights) - 1
    while True:
        if way[cur_row][cur_column] == cur_row + 1:
            rv[cur_row] += 1
            cur_column -= weights[cur_row]
        else:
            cur_row = way[cur_row][cur_column] - 1
        if way[cur_row][cur_column] == 0:
            break;
    return rv

def solve(knapsack_weigt, weights, prices):
    v = [[] for ind in range(len(weights))]
    print("0 step")
    prev_step_val = [x // weights[0] * prices[0] for x in range(0, knapsack_weigt + 1)]
    v[0] = [(lambda x: 0 if x == 0 else 1 )(e) for e in prev_step_val]
    print('v = ' + str(v))
    print(prev_step_val)
    print(len(prev_step_val))
    cur_step_val = []
    for step in range(1, len(weights)):
        cur_step_val = []
        for x in range(0, knapsack_weigt + 1):
            if x < weights[step]:
                cur_step_val.append(prev_step_val[x])
                v[step].append(v[step - 1][x])
            else:
                chose_cur = cur_step_val[x - weights[step]] + prices[step]
                if chose_cur > prev_step_val[x]:
                    v[step].append(step + 1)
                    cur_step_val.append(chose_cur)
                else:
                    v[step].append(v[step - 1][x])
                    cur_step_val.append(prev_step_val[x])
        prev_step_val = cur_step_val
        print(str(step) + " step")
        print(prev_step_val)
    print('v = ' + str(v))
    structure = calculate_structure(knapsack_weigt, v, weights)
    return cur_step_val[knapsack_weigt], structure


if __name__ == '__main__':
    print('knapsack problem')
    knapsack_weigt = 17
    weights = [3, 4, 5]
    prices = [4, 6, 7]
    solution = solve(knapsack_weigt, weights, prices)
    print(solution)
