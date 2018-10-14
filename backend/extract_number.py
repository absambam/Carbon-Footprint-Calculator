
def extract_number(s):
    tmp = s.split(" ")
    try:
        number = tmp[0].float()
    except:
        exit()
    return number
