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

    fmt.Println("Enter a value for the beginning of the range")
    fmt.Scanf("%d", &somenum)

    fmt.Println("Now enter a value for the end of the range")
    fmt.Scanf("%d", &endnum)

    for endnum < somenum {
        fmt.Println("End of range has to be be larger than the beginning of the range")
        fmt.Scanf("%d", &endnum)
        continue
    }

//    if endnum < somenum {
//        fmt.Println("End of range has to be be larger than the beginning of the range")
//    }

    finalrange := random_int(somenum, endnum)
    fmt.Println(finalrange)
}
