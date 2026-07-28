// LeetCode 1043 - Partition Array for Maximum Sum
// https://leetcode.com/problems/partition-array-for-maximum-sum/

func maxSumAfterPartitioning(arr []int, k int) int {
	n := len(arr)
	dp := make([]int, n+1)
	for i := 1; i <= n; i++ {
		best := 0
		limit := k
		if i < k {
			limit = i
		}
		for size := 1; size <= limit; size++ {
			if arr[i-size] > best {
				best = arr[i-size]
			}
			if v := dp[i-size] + best*size; v > dp[i] {
				dp[i] = v
			}
		}
	}
	return dp[n]
}
