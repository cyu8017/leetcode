// LeetCode 3500 - Minimum Cost to Divide Array Into Subarrays
// https://leetcode.com/problems/minimum-cost-to-divide-array-into-subarrays/

func minimumCost(nums []int, cost []int, k int) int64 {
	n := len(nums)
	pn := make([]int64, n+1)
	pc := make([]int64, n+1)
	for i := 0; i < n; i++ {
		pn[i+1] = pn[i] + int64(nums[i])
		pc[i+1] = pc[i] + int64(cost[i])
	}
	const inf int64 = 1 << 62
	dp := make([]int64, n+1)
	for i := 0; i < n; i++ {
		dp[i] = inf
	}
	for i := n - 1; i >= 0; i-- {
		for j := i; j < n; j++ {
			cand := pn[j+1]*(pc[j+1]-pc[i]) + int64(k)*(pc[n]-pc[i]) + dp[j+1]
			if cand < dp[i] {
				dp[i] = cand
			}
		}
	}
	return dp[0]
}
