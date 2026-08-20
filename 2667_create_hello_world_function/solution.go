// LeetCode 2667 - Create Hello World Function
// https://leetcode.com/problems/create-hello-world-function/


func createHelloWorld() func(...interface{}) string {
	return func(args ...interface{}) string {
		return "Hello World"
	}
}
