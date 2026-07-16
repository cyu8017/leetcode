// LeetCode 0172 - Factorial Trailing Zeroes
// https://leetcode.com/problems/factorial-trailing-zeroes/

func trailingZeroes(n int) int {
	count := 0
	for n > 0 {
		n /= 5
		count += n
	}
	return count
}