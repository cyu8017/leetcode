// LeetCode 0509 - Fibonacci Number
// https://leetcode.com/problems/fibonacci-number/

func fib(n int) int {
	if n <= 1 {
		return n
	}
	previous, current := 0, 1
	for index := 2; index <= n; index++ {
		previous, current = current, previous+current
	}
	return current
}
