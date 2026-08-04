// LeetCode 1553 - Minimum Number of Days to Eat N Oranges
// https://leetcode.com/problems/minimum-number-of-days-to-eat-n-oranges/

func minDays(n int) int {
	memo := map[int]int{}
	var dp func(int) int
	dp = func(x int) int {
		if x <= 1 {
			return x
		}
		if v, ok := memo[x]; ok {
			return v
		}
		a := x%2 + dp(x/2)
		b := x%3 + dp(x/3)
		if a > b {
			a = b
		}
		memo[x] = 1 + a
		return memo[x]
	}
	return dp(n)
}
