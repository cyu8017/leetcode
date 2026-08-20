// LeetCode 0718 - Maximum Length of Repeated Subarray
// https://leetcode.com/problems/maximum-length-of-repeated-subarray/

func findLength(nums1 []int, nums2 []int) int {
	m, n := len(nums1), len(nums2)
	dp := make([]int, n+1)
	best := 0
	for i := 1; i <= m; i++ {
		next := make([]int, n+1)
		for j := 1; j <= n; j++ {
			if nums1[i-1] == nums2[j-1] {
				next[j] = dp[j-1] + 1
				if next[j] > best {
					best = next[j]
				}
			}
		}
		dp = next
	}
	return best
}
