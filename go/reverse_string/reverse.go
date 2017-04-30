package main

import "fmt"

func Reverse(input string) string {
    n := 0
    rune := make([]rune, len(input))

    for _, r := range input {
      rune[n] = r
      n++
    }

    rune = rune[0:n] // decimal values

    for i := 0; i < n/2; i++ {
      rune[i], rune[n-1-i] = rune[n-1-i], rune[i]
    }

    // Convert back to UTF-8.
    output := string(rune)
    return output
}

func Revtwo(s string) string {
    r := []rune(s)
    for i, j := 0, len(r)-1; i < len(r)/2; i, j = i+1, j-1 {
        r[i], r[j] = r[j], r[i]
    }
    return string(r)
}

func main() {
  var input string

	// Reverse works on numbers, letters, kanji, blank spaces, etc. Since they're all formatted as a string.
  fmt.Println("\nEnter a string to reverse")
  fmt.Scanf("%s", &input)

	fmt.Println(Reverse(input))
	fmt.Println(Revtwo(input))
}
