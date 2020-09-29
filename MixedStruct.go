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
import "fmt"

//export GenStruct
func GenStruct(length C.int) *C.CStruct {
	valuesPointer := C.malloc(C.sizeof_char * C.size_t(length))
	valuesSlice := (*[1 << 30]C.long)(valuesPointer)[:int(length):int(length)]
	for i := 0; i < int(length); i++ {

		valuesSlice[i] = C.long(i)
	}
	i := 1
	if i > 1000 {
		fmt.Println(valuesSlice)
	}
	rtn := (*C.CStruct)(C.malloc(C.sizeof_CStruct))
	rtn.length = length
	rtn.data = valuesPointer
	return rtn
}
func main() {
}
