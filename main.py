import csv

from hashtable import HashTable, HashTableSeparateChaining, _hash_key

if __name__ == "__main__":
    ht = HashTableSeparateChaining(15)
    # 1. Extract the records from the student_data file and add them one
    # at a time, as a Python dict, containing the name, class and their
    # associated data as key-value dict pairs, to the hashtable

    # 2. You can use the id as the hash table key for each of the above
    # records.
    data = []
    with open("student-data.csv", "r") as f:
        for record in csv.DictReader(f):
            data.append(record)
    for record in data:
        # print(record["id"], _hash_key(record["id"]) % 15)
        print("id:", {record["id"]}, "value:", record)
        ht.setitem(record["id"], record)
    print("Yuri")
    for row in ht._data:
        print(row)
