g = input("Choose what you want to convert: length, wiegth, time - ")

def convertorForLength():
    a = input("From what you what to convert: ")
    a1 = int(input(f"How many {a}: "))
    b = input("To what you what to convert: ")
    if a == 'mile' and b == 'kilometer':
        return a1 * 1.6
    elif a == 'mile' and b == 'meter':
        return a1 * 1600
    elif a == 'mile' and b == 'sentemeter':
        return a1 * 1600100
    elif a == 'mile' and b == 'milimeter':
        return a1 * 1610000
    elif a == 'kilometer' and b == 'mile':
        return a1 / 1.6
    elif a == 'kilometer' and b == 'meter':
        return a1 * 1000
    elif a == 'kilometer' and b == 'sentemeter':
        return a1 * 100000
    elif a == 'kilometer' and b == 'milimeter':
        return a1 * 1000000
    elif a == 'meter' and b == 'kilometer':
        return a1 / 1000
    elif a == 'meter' and b == 'mile':
        return a1 / 1600
    elif a == 'meter' and b == 'sentemeter':
        return a1 * 100
    elif a == 'meter' and b == 'milimeter':
        return a1 * 1000
    elif a == 'sentemeter' and b == 'kilometer':
        return a1 / 100000
    elif a == 'sentemeter' and b == 'mile':
        return a1 / 1600100
    elif a == 'sentemeter' and b == 'meter':
        return a1 / 100
    elif a == 'sentemeter' and b == 'milimeter':
        return a1 * 10
    elif a == 'milimeter' and b == 'kilometer':
        return a1 / 1000000
    elif a == 'milimeter' and b == 'mile':
        return a1 / 1610000
    elif a == 'milimeter' and b == 'meter':
        return a1 / 1000
    elif a == 'milimeter' and b == 'sentemeter':
        return a1 / 10
    
def convertorForWeight():
    a = input("From what you what to convert: ")
    a1 = int(input(f"How many {a}: "))
    b = input("To what you what to convert: ")
    if a == 'kilogram' and b == 'gram':
        return a1 * 1000
    elif a == 'kilogram' and b == 'tonne':
        return a1 / 1000
    elif a == 'tonne' and b == 'kilogram':
        return a1 * 1000
    elif a == 'tonne' and b == 'gram':
        return a1 * 1000000
    elif a == 'gram' and b == 'tonne':
        return a1 / 1000000
    elif a == 'gram' and b == 'kilogram':
        return a1 / 1000
    
def convertorForTime():
    a = input("From what you what to convert: ")
    a1 = int(input(f"How many {a}: "))
    b = input("To what you what to convert: ")
    if a == 'hour' and b == 'minute':
        return a1 * 60
    elif a == 'hour' and b == 'second':
        return a1 * 3600
    elif a == 'hour' and b == 'day':
        return a1 / 24
    elif a == 'hour' and b == 'week':
        return a1 / 168
    elif a == 'minute' and b == 'second':
        return a1 * 60
    elif a == 'minute' and b == 'hour':
        return a1 / 60
    elif a == 'minute' and b == 'week':
        return a1 / 10080
    elif a == 'minute' and b == 'day':
        return a1 /1440
    elif a == 'second' and b == 'week':
        return a1 /604800
    elif a == 'second' and b == 'hour':
        return a1 /3600
    elif a == 'second' and b == 'minute':
        return a1 /60
    elif a == 'second' and b == 'day':
        return a1 /86400
    elif a == 'second' and b == 'day':
        return a1 /86400
    elif a == 'day' and b == 'second':
        return a1 * 86400
    elif a == 'day' and b == 'week':
        return a1 /7
    elif a == 'day' and b == 'minute':
        return a1 * 1440
    elif a == 'day' and b == 'hour':
        return a1 * 24
    elif a == 'week' and b == 'second':
        return a1 * 604800
    elif a == 'week' and b == 'day':
        return a1 * 7
    elif a == 'week' and b == 'minute':
        return a1 * 10080
    elif a == 'week' and b == 'hour':
        return a1 * 168
    
    

match g:
    case "length":
        print(convertorForLength())
    case "weigth":
        print(convertorForWeight())
    case "time":
        print(convertorForTime())