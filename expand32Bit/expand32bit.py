from complement import Complement
from float2fix import float2fix

def expandData(num,bit,type):
    if bit==8:
        num = float(num)
        if type=="W":
            num*=10
        num=float2fix(num,3,4)
    if bit==16:
        num=float2fix(float(num),7,8)

    sign=num[0]
    data=num[1:]
    res=""
    if bit==8:
       data="000000000000000000000000"+data
    if bit==16:
       data="0000000000000000"+data
    if type=="A":
        data=Complement(sign,data)

    res=sign+data
    return res

def ChangeDataBy8bit(fileName,saveName,bit,type):

    FromFile=open(fileName,"r")
    ToFile=open(saveName,"a")
    data=FromFile.readlines()
    for d in data:
        res=expandData(d.strip("\n"), bit, type)
        ToFile.write(res)
        ToFile.write("\n")
    FromFile.close()
    ToFile.close()

if __name__ == '__main__':

    bit= 16
    model="DCPDN"
    url="data/16-bit/"+model

    ChangeDataBy8bit(url+"/data.txt",url+"/res/data.txt",bit,"A")
    ChangeDataBy8bit(url+"/weight.txt", url+"/res/weight.txt", bit, "W")
    print("Finish")

