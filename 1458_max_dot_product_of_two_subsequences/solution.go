// LeetCode 1458 - Max Dot Product of Two Subsequences
// https://leetcode.com/problems/max-dot-product-of-two-subsequences/

func maxDotProduct(nums1 []int, nums2 []int) int {
	n := len(nums2)
	const negInf = int(-1e18)
	dp := make([]int, n+1)
	for i := range dp {
		dp[i] = negInf
	}
	for _, a := range nums1 {
		prev := append([]int(nil), dp...)
		for j, b := range nums2 {
			jj := j + 1
			product := a * b
			best := dp[jj-1]
			if prev[jj] > best {
				best = prev[jj]
			}
			if product > best {
				best = product
			}
			alt := product
			if prev[jj-1] > 0 {
				alt += prev[jj-1]
			}
			if alt > best {
				best = alt
			}
			dp[jj] = best
		}
	}
	return dp[n]
}
