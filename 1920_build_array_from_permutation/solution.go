// LeetCode 1920 - Build Array from Permutation
// https://leetcode.com/problems/build-array-from-permutation/

func buildArray(nums []int) []int {
	ans := make([]int, len(nums))
	for i, x := range nums {
		ans[i] = nums[x]
	}
	return ans
}
