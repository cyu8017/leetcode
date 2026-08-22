// LeetCode 3627 - Maximum Median Sum of Subsequences of Size 3
// https://leetcode.com/problems/maximum-median-sum-of-subsequences-of-size-3/

func maximumMedianSum(nums []int) (ans int64) {
	sort.Ints(nums)
	n := len(nums)
	for i := n / 3; i < n; i += 2 {
		ans += int64(nums[i])
	}
	return
}
