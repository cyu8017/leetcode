// LeetCode 2221 - Find Triangular Sum of an Array
// https://leetcode.com/problems/find-triangular-sum-of-an-array/

func triangularSum(nums []int) int {
	for len(nums) > 1 {
		next := make([]int, len(nums)-1)
		for i := 0; i < len(next); i++ {
			next[i] = (nums[i] + nums[i+1]) % 10
		}
		nums = next
	}
	return nums[0]
}
