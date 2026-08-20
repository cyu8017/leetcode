// LeetCode 3925 - Concatenate Array With Reverse
// https://leetcode.com/problems/concatenate-array-with-reverse/

func concatWithReverse(nums []int) []int {
	n := len(nums)
	ans := make([]int, 2*n)
	for i, x := range nums {
		ans[i] = x
		ans[i+n] = nums[n-i-1]
	}
	return ans
}
