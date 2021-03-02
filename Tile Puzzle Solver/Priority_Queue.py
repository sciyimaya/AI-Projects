
# this class implements a priority queue where nodes are sorted based on their f-values from lowest to highest
class Priority_Queue:

    def __init__(self):
        self.my_queue = list()

    # inserts a new node into the queue by following the convention where f-values go from lowest to highest
    def insert(self, new_node):
        if len(self.my_queue) != 0:
            for current_node in range(0, len(self.my_queue)):
                if new_node.f_val >= self.my_queue[current_node].f_val:
                    if current_node == (len(self.my_queue) - 1):
                        self.my_queue.insert(current_node + 1, new_node)
                    else:
                        continue
                else:
                    self.my_queue.insert(current_node, new_node)
        else:
            self.my_queue.append(new_node)

    # removes and returns the first element of the queue
    def pop(self):
        return self.my_queue.pop(0)
