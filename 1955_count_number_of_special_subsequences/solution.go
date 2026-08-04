// LeetCode 1955 - Count Number of Special Subsequences
// https://leetcode.com/problems/count-number-of-special-subsequences/

func countSpecialSubsequences(nums []int) int {
	const MOD = 1000000007
	a, b, c := 0, 0, 0
	for _, x := range nums {
		if x == 0 {
			a = (a*2 + 1) % MOD
		} else if x == 1 {
			b = (b*2 + a) % MOD
		} else {
			c = (c*2 + b) % MOD
		}
	}
	return c
}
