# go_python_struct

An example to generate complex structs in Go / cgo and return them to Python using CTypes

1. Clone the repo

`git clone https://github.com/danhitchcock/go_python_struct.git`

2. CD to the directory

`cd go_python_struct`

3. Build and run

`go build -o MixedStruct.so -buildmode=c-shared MixedStruct.go && python MixedStruct.py`
