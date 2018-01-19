def series_sum(n):
    sum = 0
    for iter in range(0,n,3):
        sum += 1/iter
    return "%.2f" % sum

def series_sum2(n):
    return '{:.2f}'.format(sum(1.0/(3 * i + 1) for i in range(n)))