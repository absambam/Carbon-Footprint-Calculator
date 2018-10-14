def extract_number(s):
    tmp = s.split(" ")
    # if the number exceeds 999, remove commas from number
    tmp2 = tmp[0].replace(",","")
    try:
        number = float(tmp2)
    except:
        return -1
    return number
