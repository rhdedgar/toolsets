package main

import (
  "fmt"
	"io"
	"net/http"
)

type Handle func(http.ResponseWriter, *http.Request, url.Values)

// Router name says it all.
type Router struct {
  tree        *node
  rootHandler Handle
}

func New(rootHandler Handle) *Router {
  node := node{component: "/", isNamedParam: false, methods: make(map[string]Handle)}
  return &Router{tree: &node, rootHandler: rootHandler}
}

//func hello(w http.ResponseWriter, r *http.Request) {
//	io.WriteString(w, "Main page")
//}
//
//func watch(w http.ResponseWriter, r *http.Request) {
//	io.WriteString(w, "Watch page")
//}
//
//func main() {
//  fmt.Println("Starting Program")
//	http.HandleFunc("/", hello)
//	http.ListenAndServe(":8000", nil)
//
