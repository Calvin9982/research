def Complement(sign,data):
    if sign=="0":
        return data
    else:
        if data=="0000000000000000000000000000000":
            return data
        list=[]
        for d in data:
            list.append(int(d))
        size=len(list)-1
        res=0
        k=1
        while(size>-1):
            res+=(k*list[size])
            k*=2
            size-=1
        res=str(bin((-res) & 0xffffffff))
        return res[3:]

