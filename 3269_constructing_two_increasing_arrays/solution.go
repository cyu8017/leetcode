// LeetCode 3269 - Constructing Two Increasing Arrays
// https://leetcode.com/problems/constructing-two-increasing-arrays/

func minLargest(nums1 []int, nums2 []int) int {
	n, m := len(nums1), len(nums2)
	const inf = int(1e9)
	dp := make([][]int, n+1)
	for i := range dp {
		dp[i] = make([]int, m+1)
		for j := range dp[i] {
			dp[i][j] = inf
		}
	}
	dp[0][0] = 0
	for i := 0; i <= n; i++ {
		for j := 0; j <= m; j++ {
			if dp[i][j] == inf {
				continue
			}
			prev := dp[i][j]
			if i < n {
				need := prev + 1
				if nums1[i] == 1 && need%2 == 0 {
					need++
				}
				if nums1[i] == 0 && need%2 == 1 {
					need++
				}
				// nums1[i]==0 means even, 1 means odd
				if nums1[i] == 0 {
					if need%2 != 0 {
						need++
					}
				} else {
					if need%2 == 0 {
						need++
					}
				}
				if need < dp[i+1][j] {
					dp[i+1][j] = need
				}
			}
			if j < m {
				need := prev + 1
				if nums2[j] == 0 {
					if need%2 != 0 {
						need++
					}
				} else {
					if need%2 == 0 {
						need++
					}
				}
				if need < dp[i][j+1] {
					dp[i][j+1] = need
				}
			}
		}
	}
	return dp[n][m]
}
