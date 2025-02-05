#this is a very basic Bubble Sort python program

my_list = [54,1,6,32,97,2]
print("Before sorting element from the list: ", my_list)
swapped = True

while swapped:
    swapped = False
    for i  in range (len(my_list) - 1):
        if my_list[i] > my_list[i + 1]:
            swapped = True
            my_list[i],my_list[i+1] = my_list[i+1] , my_list[i]

print("After swapping the elements : " ,  my_list)
