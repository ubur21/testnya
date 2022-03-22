import requests

def getRates(cur):
    rt = requests.get(url="https://api.frankfurter.app/latest?from={}".format(cur))
    return rt.json()["rates"]

def convert(list):
    result = []
    rates = getRates("USD")
    for item in list:
        result.append(item["amount"]/rates[item["currency"]]) if item["currency"] in rates else None
    return result


if __name__ == '__main__':
    # list = [1, 2, 4, 5, 6, 9, 0, 34, 56, 89, 31, 42]
    list = [{"amount":25000, "currency":"IDR"}, {"amount":200, "currency":"EUR"}]
    result = convert(list)
    print(result)
