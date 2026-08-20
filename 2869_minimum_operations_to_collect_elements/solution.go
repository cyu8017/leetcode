// LeetCode 2869 - Minimum Operations to Collect Elements
// https://leetcode.com/problems/minimum-operations-to-collect-elements/

func minOperations(nums []int, k int) int {
	need := map[int]bool{}
	for i := 1; i <= k; i++ {
		need[i] = true
	}
	for i := len(nums) - 1; i >= 0; i-- {
		delete(need, nums[i])
		if len(need) == 0 {
			return len(nums) - i
		}
	}
	return len(nums)
}
