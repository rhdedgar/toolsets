package main

import (
    "crypto/rand"
    "encoding/base32"
    "fmt"
)

func main() {
    token := getToken(10) // change to length of token wanted
    fmt.Println("Here is a random token : ", token)
}

func getToken(length int) string {
    randomBytes := make([]byte, 32) // change to byte length wanted
    _, err := rand.Read(randomBytes)
    if err != nil {
        panic(err)
    }

    // with byte count of 32, returns 56 chars, cut by length input
    // input up to 56, slice bounds out of range if any higher
    // 4RKRIYE3MHQG7QU4V7JZ7FNBTZWJLTXDDVNLMJUUKMUOC6WKB2JA====
    // byte count of 64 results in a 104-char string with no cuts
    // XAAZVTAIENGC5K6A6PTHR2KH6SAIOWMUAXM2OXKJGDE7T4HDWAQLKIQOHTMGRTZCO4EVXT4O7JQRRSAPXH3DGZSEFBADZNHFWCZT5EY=
    return base32.StdEncoding.EncodeToString(randomBytes)[:length]
}
