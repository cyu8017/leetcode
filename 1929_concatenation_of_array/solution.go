// LeetCode 1929 - Concatenation of Array
// https://leetcode.com/problems/concatenation-of-array/

func getConcatenation(nums []int) []int {
	ans := make([]int, 2*len(nums))
	copy(ans, nums)
	copy(ans[len(nums):], nums)
	return ans
}
