from collections import deque

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.queue = deque(maxlen=capacity)
        self.hash = {}
        self.capacity = capacity

    def get(self, key):
        """
        :rtype: int
        """
        if key in self.hash:
            self.queue.remove(key)
            self.queue.append(key)
            return self.hash[key]
        else:
            return -1

    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.hash:
            self.queue.remove(key)
            self.queue.append(key)
            self.hash[key] = value
        else:
            if len(self.queue) == self.capacity:
                item = self.queue.popleft()
                del self.hash[item]
            self.queue.append(key)
            self.hash[key] = value

cache = LRUCache(2)

cache.set('2', '1')
print cache.get('2')

cache.set('2', '2')
print cache.get('2')

cache.set('1', '1')
print cache.get('1')
print cache.get('2')

cache.set('4', '1')
print cache.get('1')
print cache.get('2')
print cache.get('4')

