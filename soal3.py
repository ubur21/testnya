pecahan = 1000, 2000, 5000, 10000, 20000, 50000, 100000

def closest_value(input_value):

    difference = lambda pecahan: abs(pecahan - input_value)

    res = min(pecahan, key=difference)

    return res

def greather_then(input_value):
    idx = pecahan.index(input_value)
    return pecahan[idx+1] if input_value != pecahan[len(pecahan)-1] else input_value


def test():
    result = []
    a = 39000
    lembar = 2

    sisa = a
    sisa_lembar = lembar
    while sisa_lembar > 0:
        bagi = sisa / sisa_lembar
        cl = closest_value(bagi)
        if sisa%cl==0 and cl * sisa_lembar == a:
            for i in range(0,sisa_lembar):
                result.append(cl)
                sisa = sisa - cl
                sisa_lembar = sisa_lembar - 1
        else:
            if sisa_lembar == 1:
                cl = closest_value(sisa)
                if sum(result) + cl < a:
                    cl = greather_then(cl)
                result.append(cl)
                sisa = sisa - cl
                sisa_lembar = sisa_lembar - 1
            else:
                cl = cl if (cl + sum(result)) == a else greather_then(cl)
                result.append(cl)
                sisa = sisa - cl
                sisa_lembar = sisa_lembar - 1
    return result





if __name__ == '__main__':
    # list = [1, 2, 4, 5, 6, 9, 0, 34, 56, 89, 31, 42]
    list = [3, 4, 6, 17, 25, 21, 23]
    result = test()
pecahan = 1000, 2000, 5000, 10000, 20000, 50000, 100000

def closest_value(input_value):

    difference = lambda pecahan: abs(pecahan - input_value)

    res = min(pecahan, key=difference)

    return res

def greather_then(input_value):
    idx = pecahan.index(input_value)
    return pecahan[idx+1] if input_value != pecahan[len(pecahan)-1] else input_value


def test(jmluang, jmllembar):
    result = []
    a = jmluang
    lembar = jmllembar

    sisa = a
    sisa_lembar = lembar
    while sisa_lembar > 0:
        bagi = sisa / sisa_lembar
        cl = closest_value(bagi)
        if sisa%cl==0 and cl * sisa_lembar == a:
            for i in range(0,sisa_lembar):
                result.append(cl)
                sisa = sisa - cl
                sisa_lembar = sisa_lembar - 1
        else:
            if sisa_lembar == 1:
                cl = closest_value(sisa)
                if sum(result) + cl < a:
                    cl = greather_then(cl)
                result.append(cl)
                sisa = sisa - cl
                sisa_lembar = sisa_lembar - 1
            else:
                cl = cl if (cl + sum(result)) == a else greather_then(cl)
                result.append(cl)
                sisa = sisa - cl
                sisa_lembar = sisa_lembar - 1
    return result





if __name__ == '__main__':
    result = test(30000, 3)
    print(result)
