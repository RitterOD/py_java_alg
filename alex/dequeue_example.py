

class DequeueExample:
    def __init__(self, amount):
        self.rep = [0] * amount
        self.current_size = 0
        self.front_index = 0
        self.back_index = -1

    def __str__(self):
        rv = 'Deq size : ' + str(len(self.rep)) + '\n'
        rv += 'Deq rep = ' + str(self.rep)
        return rv

    def push_front(self, elem):
        if self.current_size == len(self.rep):
            return 'Error'
        else:
            self.rep[self.front_index] = elem
            self.front_index = (self.front_index + 1) % len(self.rep)
            self.current_size += 1

    def pop_front(self):
        if self.current_size == 0:
            return 'Error'
        else:
            new_front_index = (self.front_index + len(self.rep) - 1) % len(self.rep)
            rv = self.rep[new_front_index]
            self.front_index = new_front_index
            self.current_size -= 1
            return rv


if __name__ == '__main__':
    print('Deque example')
    aDeq = DequeueExample(5)
    print(aDeq)
    rv = aDeq.push_front(1)
    print(aDeq)
    aDeq.push_front(2)
    print(aDeq)
    aDeq.push_front(3)
    print(aDeq)
    aDeq.push_front(4)
    print(aDeq)
    aDeq.push_front(5)
    print(aDeq)
    aDeq.push_front(6)
    print(aDeq)