package main

import "fmt"

func main() {
	fmt.Println("hello world")
	a := 3
	b := 2
	a, b = minMax(a, b)
	fmt.Printf("Min is %d.\n", a)
	fmt.Printf("Max is %d.\n", b)
}

func minMax(a, b int) (int, int) {
	if a >= b {
		return b, a
	}
	return a, b
}
