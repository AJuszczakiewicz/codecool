lst = [False]*100

step = 1
for n in range(0,100):
    for i in range(step-1,100, step):
        lst[i] = not lst[i]
    step += 1

open = [] 
for door in range(0,100):
    if lst[door]:
        open.append(door+1)

print(open)