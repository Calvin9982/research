import numpy as np
from floatTobin import to
from IEEE754 import ieee_754_conversion

def change(filename,toFile):
    f1 = open(filename,"r")
    f2 = open(toFile,"w")
    Data = f1.readlines()

    i=0
    for d in Data:
        str = d.strip("\n")
        i+=1
        if str == "0.0" or str == "0" or str == "0.00000000" or str == "-0.00000000":
            res = "00000000000000000000000000000000"
        else:
            k = np.float(str)
            res = to(k)
            print(i)
            print(k)
        f2.write(res)
        f2.write("\n")
    f1.close()
    f2.close()

if __name__ == '__main__':

    ## 第一个路径是要转化的数据路径
    ## 第二个是转化后保存的路径
    ## 使用的时候，只要把路径改了就行

    change("cartoonGAN/data.txt", "cartoonGAN/binary/data.txt")

    change("cartoonGAN/weight.txt", "cartoonGAN/binary/weight.txt")

    print("Finish")