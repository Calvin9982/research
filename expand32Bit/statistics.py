from float2fix import float2fix


def cal(str):
    sum = 0
    for s in str:
        if s == "0":
            sum += 1
    return sum


# 统计Weight
def getSum(bit, model, type):
    url = "data/" + str(bit) + "-bit/" + model
    if type == "W":
        Url = url + "/weight.txt"
    if type == "A":
        Url = url + "/data.txt"
    print(Url)
    file = open(Url, "r")
    weight = file.readlines()
    res = 0
    all = 0
    zero = 0
    for w in weight:
        if (w.strip("\n") == "0") or (w.strip("\n") == "0.0"):
            zero += 1
        data = float(w.strip("\n")) * 10
        if bit == 8:
            k = float2fix(data, 3, 4)
        if bit == 16:
            k = float2fix(data, 7, 8)
        times = cal(k)
        all += len(k)
        res += times
    file.close()

    res1 = zero / len(weight)
    res2 = res / all

    file = open((url + "/res.txt"), "a")

    if type == "W":
        file.write("0-ratio（weight）:  ")
        file.write(str(round(res1, 4)) + "\n")

        file.write("0-bit（weight）: ")
        file.write(str(round(res2, 4)) + "\n")

    if type == "A":
        file.write("0-ratio（data）:  ")
        file.write(str(round(res1, 4)) + "\n")

        file.write("0-bit（data）: ")
        file.write(str(round(res2, 4)) + "\n")

    file.close()


if __name__ == '__main__':
    bit = 16
    model = "FCOS"
    getSum(bit, model, "W")
    getSum(bit, model, "A")
    print("Finish")
