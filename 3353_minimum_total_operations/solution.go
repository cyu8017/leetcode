// LeetCode 3353 - Minimum Total Operations
// https://leetcode.com/problems/minimum-total-operations/

func minimumOperations(nums []int) int {
	// each time set all equal to nums[i] for some suffix? Problem: make all equal by choosing index i and setting all from 0..i to nums[i]
	// actually: operation: choose i, set nums[0..i]=nums[i]. Min ops to make all equal.
	ops := 0
	for i := len(nums) - 2; i >= 0; i-- {
		if nums[i] != nums[i+1] {
			ops++
		}
	}
	return ops
}
