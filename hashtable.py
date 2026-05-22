from bucket import Bucket


def _hash_key(key: str, p: int = 53) -> int:
    """Hashes the key using the rolling polynomial algorithm.

    Arguments:
    - key: str
      The key to be hashed.
    - p: int
      A prime number used for the rolling polynomial algorithm

    Returns:
    - the hashed location (int)
    """
    total = 0
    for i, char in enumerate(key):
        total += ord(char) * p**i
    return total


class HashTable:
    """A hashtable without collision resolution.

    Arguments:
    - size: int
      The number of slots that the hash table is initialised with

    Attributes:
    - size: int
      The number of slots that the hash table has
    - length: int
      The number of records contained in the hash table
    """

    def __init__(self, size: int):
        self.size = size
        self.length = 0
        self._data: list = [None] * size

    def __repr__(self) -> str:
        return f"HashTable(size={self.size})"

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.
        """
        hash: int = _hash_key(key) % self.size
        if self._data[hash] is None:
            self.length += 1
        self._data[hash] = value

    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        hash: int = _hash_key(key) % self.size
        value: dict = self._data[hash]
        if value is None:
            raise KeyError
        return value

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        hash: int = _hash_key(key) % self.size
        value: dict = self._data[hash]
        if value is None:
            raise KeyError
        self._data[hash] = None
        self.length -= 1


class HashTableLinearProbing(HashTable):
    """A hashtable that implements collision resolution using
    linear probing.

    Arguments:
    - size: int
      The number of slots that the hash table is initialised with
    """

    # Values are stored as a 2 element tuple (key, value)

    def __init__(self, size: int):
        super().__init__(size)
        # Add your code here

    def __repr__(self) -> str:
        return f"HashTableLinearProbing(size={self.size})"

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.
        """
        hash: int = _hash_key(key) % self.size
        safety = 0
        current = self._data[hash]
        while current is not None and current[0] != key:
            hash += 1
            hash %= self.size
            current = self._data[hash]
            safety += 1
            if safety >= self.size:
                # full hashtable, idk what to do girlll
                break

        if self._data[hash] is None:
            self.length += 1
        self._data[hash] = (key, value)

    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        hash: int = _hash_key(key) % self.size
        safety = 0
        current = self._data[hash]
        while current is not None and current[0] != key:
            hash += 1
            hash %= self.size
            current = self._data[hash]
            safety += 1
            if safety >= self.size:
                # full hashtable, idk what to do girlll
                break

        value: dict = self._data[hash]
        if value is None:
            raise KeyError
        return value

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        hash: int = _hash_key(key) % self.size
        safety = 0
        current = self._data[hash]
        while current is not None and current[0] != key:
            hash += 1
            hash %= self.size
            current = self._data[hash]
            safety += 1
            if safety >= self.size:
                # full hashtable, idk what to do girlll
                break

        value: dict = self._data[hash]
        if value is None:
            raise KeyError
        self._data[hash] = None


class HashTableSeparateChaining(HashTable):
    """A hashtable that implements collision resolution using
    separate chaining.

    Arguments:
    - size: int
      The number of slots that the hash table is initialised with
    """

    def __init__(self, size: int):
        super().__init__(size)
        self._data: list[Bucket] = [Bucket() for i in range(size)]

        # Add your code here

    def __repr__(self) -> str:
        return f"HashTableLinearProbing(size={self.size})"

    def setitem(self, key: str, value: dict) -> None:
        """Stores key and value in the hash table.

        If the key already exists in the hash table, the existing value
        is overwritten.
        """
        hash: int = _hash_key(key) % self.size
        self._data[hash].add((key, value))

    def getitem(self, key: str) -> dict:
        """Retrieves the value associated with key, and returns it.

        If the key does not exist, a KeyError is raised.
        """
        hash: int = _hash_key(key) % self.size
        bucket: Bucket = self._data[hash]
        return bucket.get(key)[1]

    def delitem(self, key: str) -> None:
        """Deletes the key and its associated value from the hash table.

        If the key does not exist, a KeyError is raised.
        """
        hash: int = _hash_key(key) % self.size
        bucket: Bucket = self._data[hash]
        bucket.delete(key)


if __name__ == "__main__":
    # this is so evil!!!!
    table = HashTable(15)
    table.setitem("sb", {"a": 1})
    print(table.getitem("sb"))
