// LeetCode 3473 - Sum of K Subarrays With Length at Least M
// https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

func maxSum(nums []int, k int, m int) int {
	n := len(nums)
	pref := make([]int, n+1)
	for i, x := range nums {
		pref[i+1] = pref[i] + x
	}
	const neg = -1 << 60
	dp := make([][]int, k+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
		for j := range dp[i] {
			dp[i][j] = neg
		}
	}
	dp[0][0] = 0
	for i := 0; i <= n; i++ {
		dp[0][i] = 0
	}
	for t := 1; t <= k; t++ {
		best := neg
		for i := t * m; i <= n; i++ {
			// best of dp[t-1][j] - pref[j] for j <= i-m
			j := i - m
			if dp[t-1][j]-pref[j] > best {
				best = dp[t-1][j] - pref[j]
			}
			dp[t][i] = best + pref[i]
			if dp[t][i-1] > dp[t][i] {
				// allow not ending at i - actually need max over ends
			}
		}
		for i := 1; i <= n; i++ {
			if dp[t][i-1] > dp[t][i] {
				dp[t][i] = dp[t][i-1]
			}
		}
	}
	return dp[k][n]
}
