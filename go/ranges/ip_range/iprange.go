package main

import (
    "fmt"
    "strconv"
)

func main() {
    fmt.Println("Placeholder text.")

    // type, length, capacity
    // make length = 0 so there aren't 65536 blank spaces before the actual rules
    ip_slice := make([]string, 0, 65536)

    for i := 0; i < 256; i++ {
        for j := 0; j < 256; j++ {
            // reassigning the value of ipslice works like += in this case
            ip_slice = append(ip_slice, "10.0." + strconv.Itoa(i) + "." + strconv.Itoa(j))
        }
    }

    //fmt.Println(ip_slice)
    for _, x := range ip_slice {
        fmt.Println(x)
    }

    fmt.Println("total number of rules: ", len(ip_slice))

}
