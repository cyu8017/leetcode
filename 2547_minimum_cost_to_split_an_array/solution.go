// LeetCode 2547 - Minimum Cost to Split an Array
// https://leetcode.com/problems/minimum-cost-to-split-an-array/


func minCost(nums []int, k int) int {
	n := len(nums)
	const INF = int(1e18)
	dp := make([]int, n+1)
	for i := 1; i <= n; i++ {
		dp[i] = INF
	}
	for i := 0; i < n; i++ {
		freq := map[int]int{}
		trimmed := 0
		for j := i; j < n; j++ {
			freq[nums[j]]++
			c := freq[nums[j]]
			if c == 2 {
				trimmed += 2
			} else if c > 2 {
				trimmed++
			}
			cost := dp[i] + k + trimmed
			if cost < dp[j+1] {
				dp[j+1] = cost
			}
		}
	}
	return dp[n]
}
