# Problem URL : https://www.hackerrank.com/challenges/python-lists/problem



if __name__ == '__main__':
    N = int(input())
    current_list = []
    for operations in range(N):
        input_list = []
        input_string = input()
        input_list = input_string.split()
        if input_list[0] == "insert":
            current_list.insert(int(input_list[1]) , int(input_list[2]))
        elif input_list[0] == "print":
            print(current_list)
        elif input_list[0] == "remove":
            current_list.remove(int(input_list[1]))
        elif input_list[0] == "append":
            current_list.append(int(input_list[1]))
        elif input_list[0] == "pop":
            current_list.pop()
        elif input_list[0] == "sort":
            current_list.sort()
        else:
            current_list.reverse()      
         

