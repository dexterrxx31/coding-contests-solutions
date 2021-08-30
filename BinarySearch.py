
#Binary Search Iteration Method
def BinarySearch_iteration_method(list_input, element):
    start = 0
    end = len(list_input)
    while True:
        mid = (start + end + 1)//2
        if element == list_input[mid]:
            return mid
        elif element > list_input[mid]:
            start = mid + 1
            continue
        elif element < list_input[mid]:
            end = mid - 1
            continue


#Binary Search Recusive Method
def BinarySearch_recursion_method(list_input, element, start, end):
    if end >= 1:

        mid = start + (end-1) // 2
        if element == list_input[mid]:
            return mid

        if element > list_input[mid]:
            return BinarySearch_recursion_method(list_input, element, mid + 1, end)
        if element < list_input[mid]:
            return BinarySearch_recursion_method(list_input, element, start, mid - 1)
    else:
        return -1


list_input = [23, 4, 1, 5, 78, 98]
list_input.sort()
print(list_input)
print(BinarySearch_iteration_method(list_input , 98))
print(BinarySearch_recursion_method(list_input,4, 0, len(list_input)))
