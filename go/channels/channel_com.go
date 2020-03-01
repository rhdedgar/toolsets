package main

import (
	"fmt"
)

var (
	inChan  = make(chan string)
	outChan = make(chan string)
)

func chanFunc(ichan <-chan string) { //, ochan chan<- string) {
	for {
		select {
		case readChan := <-ichan:
			newStr := readChan + "_appended"
			outChan <- newStr
			fmt.Println("Appended the string and sent it back via channel.")
		}
	}
}

func setChan(someChan chan<- string) {
	someChan <- "initial_val"
}

func main() {
	go setChan(inChan)
	go chanFunc(inChan)

	outputMsg := <-outChan
	fmt.Println(outputMsg)
}
