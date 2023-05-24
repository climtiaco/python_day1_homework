# Function 1
def hello(name):
  print("Hi, ", name)

  # Function 2
def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]


# Function 3
# Creating an argument that can later be unpacked was helpful for this piece of code.
def eat_lunch(my_list):
  if len(my_list) == 0:
    print('My lunchbox is empty')
  else:
    for i in range(len(my_list)):
        if i == 0:
          print(f"First I eat {my_list[0]}")
        else:
          print(f"Next I eat {my_list[i]}")

hello("Christian")
print(pack("lunch", "backpack", "underwear"))
eat_lunch([])
eat_lunch(["Pizza"])
eat_lunch(["crackers", "fregola", "tenderloins", "salmon"])



