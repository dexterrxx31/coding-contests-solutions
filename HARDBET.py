number_of_test_cases= int(input())
for x in range(number_of_test_cases):
    c = input().split()
    s = []
    for y in c:
        s.append(int(y))
    temp = s.copy()
    s.sort()

    if s[0] == temp[0]:
       print("Draw")
    elif s[0] == temp[1]:
       print("Bob")
    else:
       print("Alice")

