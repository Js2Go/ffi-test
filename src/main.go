package main

import "C"
import "fmt"

//export fibonacci
func fibonacci(n int32) int32 {
	return fib(n)
}

//export getData
func getData() {
	fmt.Println("hello, world")
}

func main() {}

func fib(n int32) int32 {
	if n == 0 || n == 1 {
		return n
	}
	return fib(n - 1) + fib(n - 2)
}
