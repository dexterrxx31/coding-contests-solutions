ntc = int(input())
for x in range(ntc):
    fst = list(map(int , input().split()))
    sec = list(map(int , input().split()))
    max_drug = fst[1] * (fst[2] - 1)
    N  = fst[0]
    sp_of_fnd_with_drug = sec[N-1] + max_drug
    sp_of_fnd_without_drug = sec[N-1]
    speed = 0 
    if sp_of_fnd_without_drug >= sp_of_fnd_with_drug :
        speed = sp_of_fnd_without_drug
    else:
        speed = sp_of_fnd_with_drug
    status = "Yes"
    for y in sec[:-1]:
        if y >= speed:
            status = "No"
    print(status) 
