class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []
        self.overwrite = []
    def append(self, item):
        if (len(self.buffer) < self.capacity):
            self.buffer.append(item)
        else:
            if (len(self.overwrite) == self.capacity):
                self.overwrite.clear()
            self.overwrite.append(item)
            position = (len(self.overwrite))
            self.buffer[position - 1] = item

    def get(self):
        return self.buffer