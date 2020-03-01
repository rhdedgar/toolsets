package main

import (
    "fmt"
    "math/rand"
    "time"
    "strings"
    "strconv"
)
// for i in random, append a random number to that random-length slice

func random_int(min, max, seed int) int {
    if min == 0 && max == 0 {
      max = 100
    }

    if seed == 0 {
        rand.Seed(time.Now().Unix())
    }

    return rand.Intn(max - min) + min
}


func main() {

    new_time := time.Now().Unix()
    orig_seed := int(new_time)

    // or use rand_slice := make([]int, random_int(0, 0, orig_seed))
    var rand_slice []int

    slice_length := random_int(0, 30, 0)
    // or keep index number, replace the item at that number
    for i := 0; i < slice_length; i++ { //range rand_slice {
        rand_slice = append(rand_slice, random_int(0, 50, orig_seed))
        orig_seed++
    }

    fmt.Println(rand_slice)

    stringver := strings.Trim(strings.Join(strings.Fields(fmt.Sprint(rand_slice)), ","), "[]")
    fmt.Println(stringver)

/*    var uniqmap map[int]int
    uniqmap = make(map[int]int)

    for i := range rand_slice {
        if uniqmap[i] == 0 {
            uniqmap[i] = strings.Count(stringver, strconv.FormatInt(int64(i), 10))
        }
    }
*/

    var uniqmap map[string]int
    uniqmap = make(map[string]int)


    for i := strings.Split(stringver, ",") {
        if _, ok := m[i] {
            strings.Count(stringver, i)
        }
    }

    fmt.Println(uniqmap)

}
