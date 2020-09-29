from ctypes import c_int, CDLL, Structure, c_void_p, c_double, c_long
import numpy as np
from numpy.ctypeslib import ndpointer

GO = CDLL("MixedStruct.so")


class MixedStruct(Structure):
    _fields_ = [("length", c_int), ("data", c_long)]


GO.GenStruct.argtypes = [c_int]
GO.GenStruct.restype = c_void_p


def mixed_struct(x):
    result = MixedStruct.from_address(GO.GenStruct(x))
    data = np.frombuffer((c_long * x).from_address(result.data), np.int64)
    length = result.length
    return {"Length": length, "Data": data}


if __name__ == "__main__":
    for i in range(20):
        print(mixed_struct(i))
