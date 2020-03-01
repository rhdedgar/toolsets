package main

import (
    "fmt"
    "strconv"
)

func main() {
	vals := make([]string, 5)
	for i := 0; i < 5; i++ {
		vals = append(vals, strconv.Itoa(i))
	}
	fmt.Println(vals)
}
