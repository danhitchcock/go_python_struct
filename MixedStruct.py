from ctypes import c_int, CDLL, Structure, c_void_p, c_double, c_long, POINTER
import numpy as np
from numpy.ctypeslib import ndpointer

GO = CDLL("MixedStruct.so")

# Create an object to capture the struct
class MixedStruct(Structure):
    _fields_ = [("length", c_int), ("data", c_long)]


# Define the arg and return types of the function
GO.GenStruct.argtypes = [c_int]
GO.GenStruct.restype = POINTER(MixedStruct)


def mixed_struct(x):
    # Get results as the MixedStruct class we defined above
    result = GO.GenStruct(x)
    # Create a buffer from the memory address contained in the struct as 'data' and
    # read it as np.int64
    data = np.frombuffer((c_long * x).from_address(result.contents.data), np.int64)
    length = result.contents.length
    return {"Length": length, "Data": data}


if __name__ == "__main__":
    for i in range(20):
        print(mixed_struct(i))
