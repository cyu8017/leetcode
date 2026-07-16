// LeetCode 0343 - Integer Break
// https://leetcode.com/problems/integer-break/

func integerBreak(n int) int {
	if n <= 3 {
		return n - 1
	}

	product := 1
	for n > 4 {
		product *= 3
		n -= 3
	}
	return product * n
}
