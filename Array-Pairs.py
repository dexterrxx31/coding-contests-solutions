# Find pair of inters which have given target sum


input_list = [10, 5, 2, 3, -6, 9, 11]
target_sum = 4


def finding_pairs_bruteforce(input_list, target_sum):
    result_list = []
    for x in range(len(input_list)):
        for y in range(len(input_list)):
            if input_list[y] == input_list[x]:
                continue
            if input_list[x] + input_list[y] == target_sum:
                result_list.append(input_list[x])
                result_list.append(input_list[y])
                return result_list


def BinarySearch(lys, val):
    first = 0
    last = len(lys)-1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first+last)//2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return 1


def finding_pairs_sorting(input_list, target_sum):
    input_list.sort()
    for x in range(len(input_list)):
        current_item = input_list[x]
        required_number = target_sum - current_item
        if BinarySearch(input_list, required_number):
            return (current_item, required_number)


def finding_pairs_set_method(input_list ,target_sum):
    set_of_input_list = set()
    for x in range(len(input_list)):
        current_item = input_list[x]
        required_number = target_sum - current_item
        if required_number in set_of_input_list:
            return (current_item, required_number)
        else:
            set_of_input_list.add(current_item) 

print(finding_pairs_set_method(input_list, target_sum))
