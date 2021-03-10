# (layer1): Conv2d(3, 8, kernel_size=(4, 4), stride=(2, 2), padding=(1, 1), bias=False)

data0=[1,3,2,31,54,5,8]
data1=[3,0,1,5,4,3,5]
data2=[11,32,20,61,4,7,5]
data3=[17,38,52,1,4,27,75]

flag=0
i=0

len=len(data0)
if len%2!=0:
    len-=1

while(i < len):
  flag+=1
  if flag<5 :
      print(data0[i])
      i += 1
  else:
    flag=0
    i-=2

# print("finish")