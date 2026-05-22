class Node:
    """Represents a node in a bucket.

    Arguments
        - data
          The data encapsulated in the node.

    Attributes
        - next: Node | None
          The next node in the bucket, or None if the node is the tail.

    Methods
        - get() -> data
          Return the data stored in the node.
    """

    def __init__(self, key: str, data: dict):
        self.key = key
        self.data = data
        self.next: Node | None = None

    def __repr__(self) -> str:
        return f"Node({self.key} : {self.data})"


class Bucket:
    """Represents a sequence of data items.

    Arguments
        None

    Attributes
        None

    Methods
        - length() -> int
        - get(key) -> tuple[str, dict]
        - append(item) -> None
        - delete(key) -> None
    """

    def __init__(self):
        self._head: Node | None = None

    def __repr__(self) -> str:
        dataRepr: list[str] = [repr(x) for x in self._getall()]
        return "bucket(\n" + ",\n".join(dataRepr) + "\n)"

    def _getall(self) -> list[Node]:
        acc = []
        current = self._head
        while current is not None:
            acc.append(current)
            current = current.next
        return acc

    def length(self) -> int:
        """Returns the number of nodes in the bucket.

        Arguments
            None

        Return
            length of bucket as an integer (zero or positive)
        """
        current = self._head
        size = 0
        while current is not None:
            current = current.next
            size += 1
        return size

    def get(self, key: str) -> dict:
        """gets the item with the key specified

        Arguments
            - key: str
                key to be deleted.

        Raises
            KeyError if there is no such entry
        """
        # Replace the line below with your code
        previous: Node = None
        current = self._head
        while current is not None:
            if current.key == key:
                # Set previous node to point to current's next node instead
                previous.next = current.next
                return current.data
            previous = current
            current = current.next
        raise KeyError

    def add(self, key: str, value: dict) -> None:
        """adds an entry with the specified key to the bucket, if the entry already exists, the entry is overwritten

        Arguments
            - item
              The item to be appended.

        Returns
            None
        """
        # Replace the line below with your code

        previous: Node = None
        current = self._head
        item_node = Node(key, value)
        # Empty bucket
        if current is None:
            self._head = item_node
            return
        while current.next is not None:
            if current.key == key:
                if previous is None:
                    self._data = item_node
                else:
                    previous.next = item_node
                    item_node.next = current.next
                return
            previous = current
            current = current.next
        # Did not find an existing entry, so just append it
        current.next = item_node

    def delete(self, key: str) -> None:
        """Delete n-th item from bucket.

        Arguments
            - key: str
              key to be deleted.

        Raises
            KeyError if there is no such entry
        """

        # Replace the line below with your code
        previous: Node = None
        current = self._head
        while current is not None:
            if current.key == key:
                # Set previous node to point to current's next node instead
                previous.next = current.next
                return
            previous = current
            current = current.next
        raise KeyError
