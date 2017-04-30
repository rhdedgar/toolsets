package main

import(
    "fmt"
    "math/rand"
    "time"
)


func random_int(min, max int) int {
    rand.Seed(time.Now().Unix())
    return rand.Intn(max - min) + min
}


func main() {
    fmt.Println("Printing a random number between -11 and 11 to test")
    myrand := random_int(-11, 11)
    fmt.Println(myrand)

    var somenum int
    var endnum int
    var finalrange int

    fmt.Println("\nEnter a value for the beginning of the range")
    fmt.Scanf("%d", &somenum)

    fmt.Println("\nNow enter a value for the end of the range")
    fmt.Scanf("%d", &endnum)

    if endnum < somenum {
        fmt.Println("\nEnd of range has to be be larger than the beginning of the range, swapping")
        finalrange = random_int(endnum, somenum)

    } else {
        fmt.Println("\nEnd of range is larger than beginning of range, looks good!")
        finalrange = random_int(somenum, endnum)
    }

    fmt.Println(finalrange)
}
