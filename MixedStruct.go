package main

/*
#include <stdlib.h>
typedef struct
{
    int length;
    void *data;
} CStruct;
*/
import "C"

//export GenStruct
func GenStruct(length C.int) *C.CStruct {
	// allocate memory with C.malloc
	valuesPointer := C.malloc(C.sizeof_long * C.size_t(length))
	// create an array/slice, such that the C array (values pointer) can be access
	valuesSlice := (*[1 << 30]C.long)(valuesPointer)[:int(length):int(length)]
	// assign values to the C array through the slice
	for i := 0; i < int(length); i++ {
		valuesSlice[i] = C.long(i)
	}
	//make a struct and assign values
	rtn := (*C.CStruct)(C.malloc(C.sizeof_CStruct))
	rtn.length = length
	rtn.data = valuesPointer
	return rtn
}
func main() {
}
