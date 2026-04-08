# List operations :<
my_list = [10, 20, 30, 40, 50]

my_list.append(60)
my_list.remove(30)
my_list.sort()
print(my_list)

# My tuple
my_tuple = (1, 2, 3, 4, 5)
my_tuple[0] = 10  # This will raise an error because tuples are immutable

# My set
my_set = {"apple", 2, "banana", 4, "cherry"}
my_set.add(6)
my_set.remove("banana")
print(my_set)

# My dictionary
my_dict = {"name": "ELIEZAR", "age": 21, "city": "Taguig"}
my_dict["grade"] = "COLLEGE"
my_dict.update({"age": 22})
print(my_dict)