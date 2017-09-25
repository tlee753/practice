package main

import "fmt"

func main() {
	fmt.Println("hello world")
	fmt.Println(minMax(2, 3))
}

func minMax(a, b int) (int, int) {
	if (a >= b) {
		return b, a
	}
	return a, b
}