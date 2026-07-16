// LeetCode 0263 - Ugly Number
// https://leetcode.com/problems/ugly-number/

func isUgly(n int) bool {
	if n <= 0 {
		return false
	}
	for _, factor := range []int{2, 3, 5} {
		for n%factor == 0 {
			n /= factor
		}
	}
	return n == 1
}
