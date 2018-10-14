def extract_number(s):
    tmp = s.split(" ")
    print(tmp)
    try:
        number = float(tmp[0])
        print(number)
    except:
        exit()
    return number
