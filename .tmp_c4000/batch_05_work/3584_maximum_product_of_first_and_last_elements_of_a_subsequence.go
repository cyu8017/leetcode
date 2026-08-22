// LeetCode 3584 - Maximum Product of First and Last Elements of a Subsequence
// https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/

func maximumProduct(nums []int, m int) int64 {
	ans := int64(math.MinInt64)
	mx := math.MinInt32
	mi := math.MaxInt32

	for i := m - 1; i < len(nums); i++ {
		x := nums[i]
		y := nums[i-m+1]
		mi = min(mi, y)
		mx = max(mx, y)
		ans = max(ans, max(int64(x)*int64(mi), int64(x)*int64(mx)))
	}

	return ans
}
