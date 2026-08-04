// LeetCode 1414 - Find the Minimum Number of Fibonacci Numbers Whose Sum Is K
// https://leetcode.com/problems/find-the-minimum-number-of-fibonacci-numbers-whose-sum-is-k/

func findMinFibonacciNumbers(k int) int {
	fib := []int{1, 1}
	for fib[len(fib)-1] < k {
		fib = append(fib, fib[len(fib)-1]+fib[len(fib)-2])
	}
	answer := 0
	for i := len(fib) - 1; i >= 0; i-- {
		if fib[i] <= k {
			k -= fib[i]
			answer++
		}
	}
	return answer
}
