def sockMerchant(n, ar):
    freq_of_all_letters = {}
    for i in ar:
        if i in freq_of_all_letters:
            freq_of_all_letters[i] += 1
        else:
            freq_of_all_letters[i] = 1
    counter = 0
    for key , value in freq_of_all_letters.items():
        if value % 2 == 0 :
            counter = counter + value
        else:
            counter = counter + value - 1
    return counter//2

print(sockMerchant(9,[10, 20, 20, 10, 10, 30, 50, 10, 20]))