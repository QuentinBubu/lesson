def resteDivEucl(number, start):
    return int(number//start)

def convert_to_binary(number):
    start = 2048
    result = ""
    while start != 1:
        nb = resteDivEucl(number, start)
        if result != "" or nb != 0:
            if nb == 1:
                number -= start
            result += str(nb)
        start /= 2
    result += str(resteDivEucl(number, 1))
    return result