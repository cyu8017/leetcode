// LeetCode 1827 - Minimum Operations to Make the Array Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

func minOperations(nums []int) int {
	ops := 0
	prev := nums[0]
	for _, value := range nums[1:] {
		if value <= prev {
			needed := prev + 1
			ops += needed - value
			prev = needed
		} else {
			prev = value
		}
	}
	return ops
}
