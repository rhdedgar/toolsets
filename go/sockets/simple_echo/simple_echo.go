package main

import (
	"bufio"
	"fmt"
	"net"
)

func main() {
	serverPort := ":8080"
	fmt.Println("Launching server on: ", serverPort)

	ln, _ := net.Listen("tcp", serverPort)
	conn, _ := ln.Accept()

	for {
		scanner := bufio.NewScanner(conn)
		for scanner.Scan() {
			scanOut := scanner.Text()
			fmt.Println(scanOut)
		}
		//strconv.Atoi(scanner.Text())

		//message1 := bufio.NewReader(conn) //.ReadString('\n')
		//message :=
		//	fmt.Print("Message Received:", string(message))

		//newmessage := strings.ToUpper(message)

		//conn.Write([]byte(newmessage + "\n"))
		break
	}
}
