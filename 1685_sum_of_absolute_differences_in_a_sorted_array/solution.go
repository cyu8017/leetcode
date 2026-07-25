// LeetCode 1685 - Sum of Absolute Differences in a Sorted Array
// https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/

func getSumAbsoluteDifferences(nums []int) []int {
	total := 0
	for _, x := range nums {
		total += x
	}
	n := len(nums)
	ans := make([]int, n)
	left := 0
	for i, x := range nums {
		ans[i] = x*i - left + (total - left - x) - x*(n-i-1)
		left += x
	}
	return ans
}
