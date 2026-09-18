ll = [1, 2, 3, 4, 5]

def countSum(ll):
    count = 0
    for num in ll:
        count += num
    return count


print(countSum(ll))
