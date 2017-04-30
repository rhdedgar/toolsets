package main

import (
	"fmt"
	"math/rand"
  "time"
)

func main() {
	rand.Seed(time.Now().Unix())
	fmt.Println("Magic 8-Ball says:", rand.Intn(100))
}
