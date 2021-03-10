import numpy as np
import torch
from binary_converter import float2bit
def to(d):
    data=[]
    d=np.float(d)
    data.append(d)
    f = torch.Tensor(data)
    pred = float2bit(f, num_e_bits=8, num_m_bits=23, bias=127.)
    res= ""
    l = pred.numpy().tolist()
    for k in l:
        for z in k:
            res+=str(int(z))
    return res
