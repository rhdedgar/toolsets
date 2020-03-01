package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var myname string

	scanner := bufio.NewScanner(os.Stdin)
	str1 := "What is your name?"

	for scanner.Scan() {
		fmt.Println(str1)
		myname = scanner.Text()
		fmt.Println("Hello", myname)
	}
	fmt.Println("exiting")
}
