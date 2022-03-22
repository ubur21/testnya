def median(list):
    n = len(list)
    return (list[n//2-1]/2.0+list[n//2]/2.0, list[n//2])[n % 2] if n else None

def getResult(list):
    result = []
    for item in list:
        result_item = dict(
            mean=sum(item) / len(item),
            median=median(item)
        )
        result.append(result_item)
    return  result

def getMeanMedian(list):

    arr = [[list[0]]]
    cur = 0
    curnumb = list[0]
    for i in range(1, len(list), 1):
        if list[i] > curnumb:
            arr[cur].append(list[i])
        else:
            arr.append([list[i]])
            cur += 1
        curnumb = list[i]
    return getResult(arr)


if __name__ == '__main__':
    # list = [1, 2, 4, 5, 6, 9, 0, 34, 56, 89, 31, 42]
    list = [3, 4, 6, 17, 25, 21, 23]
    result = getMeanMedian(list)
    print(result)
