def extract_number(s):
    tmp = s.split(" ")
    try:
        number = float(tmp[0])
    except:
        exit()
    return number
