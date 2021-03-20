class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if len(self.queue) < 1:
            return None
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def isEmpty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def contains(self, item):
        if len(self.queue) == 0:
            return False
        for i in range(0, len(self.queue)):
            if self.queue[i] == item:
                return True
        return False
