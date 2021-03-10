def calData(model, type):
    Url = "data/float-32/" + model
    if type == "A":
        url = Url + "/data.txt"
    if type == "W":
        url = Url + "/weight.txt"

    file = open(url, "r")
    data = file.readlines()
    zero = 0
    for d in data:
        if d.strip("\n") == "0" or d.strip("\n") == "0.0":
            zero += 1
    file.close()
    res = zero / (len(data))
    # save
    Url += "/res.txt"
    file = open(Url, "a")
    if type == "A":
        file.write("0-ratio（data）:  ")
    if type == "W":
        file.write("0-ratio（weight）:  ")
    file.write(str(round(res,4)))
    file.write("\n")
    file.close()
    return

def cal(str):
    sum = 0
    for s in str:
        if s == "0":
            sum += 1
    return sum

def calBit(model,type):
    Url = "data/float-32/" + model
    if type == "A":
        url = Url + "/binary/data.txt"
    if type == "W":
        url = Url + "/binary/weight.txt"

    file=open(url,"r")
    data=file.readlines()
    zero=0
    Len=0
    for d in data:
        Len+=len(d.strip("\n"))
        zero+=cal(d.strip("\n"))

    #save
    Url += "/res.txt"
    file = open(Url, "a")
    if type == "A":
        file.write("0-bit（data）:  ")
    if type == "W":
        file.write("0-bit（weight）:  ")
    res=zero/Len
    file.write(str(round(res, 4)))
    file.write("\n")
    file.close()

if __name__ == '__main__':
    model = "D3DNet"
    calData(model, "W")
    calBit(model,"W")
    calData(model, "A")
    calBit(model,"A")
    print("Finish")