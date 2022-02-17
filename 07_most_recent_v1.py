# Set up empty list
from numpy import allclose


all_calculations = []

# Get five items of data
get_item = ""
while get_item != input("xxx"):
    get_item = input("Enter an item: ")

    if get_item == "xxx":
        break

    all_calculations.append(get_item)
print()

if len(all_calculations) == 0:
    print("List is empty")
else:
    # Show tat everything made it to the list
    print()
    print("The FULL LIST")
    print(all_calculations)

    # print items starting at the end of the list
    if len(all_calculations) >= 3:
        print("MOST RECENT 3")
        for item in range(0,3):
            print(all_calculations[len(all_calculations)- item - 1])
    else:
        print("ITEMS FROM NEWEST TO OLDEST")
        for item in all_calculations:
            print(all_calculations[len(all_calculations) - all_calculations.index(item)])