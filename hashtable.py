#!python

from linkedlist import LinkedList

class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(self.length())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        # TODO: Count number of key-value entries in each of the buckets

        count = 0

        for index in range(len(self.buckets)):
            currentNode = self.buckets[index].head

            while currentNode != None:
                count += 1
                currentNode = currentNode.next

        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        # TODO: Check if the given key exists in a bucket

        index = self._bucket_index(key)
        currentNode = self.buckets[index].head

        while currentNode != None:
            if currentNode.data[0] == key:
                return True

            currentNode = currentNode.next

        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # TODO: Check if the given key exists and return its associated value

        index = self._bucket_index(key)
        currentNode = self.buckets[index].head

        while currentNode != None:
            if currentNode.data[0] == key:
                return currentNode.data[1]

            currentNode = currentNode.next

        raise KeyError

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        # TODO: Insert or update the given key-value entry into a bucket

        index = self._bucket_index(key)
        currentNode = self.buckets[index].head

        while currentNode != None:
            if currentNode.data[0] == key:
                currentNode.data = (key, value)
                return

            currentNode = currentNode.next


        self.buckets[index].append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # TODO: Find the given key and delete its entry if found

        index = self._bucket_index(key)
        currentNode = self.buckets[index].head

        while currentNode != None:
            if currentNode.data[0] == key:
                self.buckets[index].delete(currentNode.data)
                return

            currentNode = currentNode.next

        raise KeyError

    def keys(self):
        """Return a list of all keys in this hash table"""
        # TODO: Collect all keys in each of the buckets

        listOfKeys = []

        for index in range(len(self.buckets)):
            currentNode = self.buckets[index].head

            while currentNode != None:
                listOfKeys.append(currentNode.data[0])
                currentNode = currentNode.next

        return listOfKeys

    def values(self):
        """Return a list of all values in this hash table"""
        # TODO: Collect all values in each of the buckets

        listOfValues = []

        for index in range(len(self.buckets)):
            currentNode = self.buckets[index].head

            while currentNode != None:
                listOfValues.append(currentNode.data[1])
                currentNode = currentNode.next

        return listOfValues
