// LeetCode 0213 - House Robber II
// https://leetcode.com/problems/house-robber-ii/

func robLinear(nums []int) int {
	previousTwo, previousOne := 0, 0
	for _, value := range nums {
		current := previousOne
		if previousTwo+value > current {
			current = previousTwo + value
		}
		previousTwo, previousOne = previousOne, current
	}
	return previousOne
}

func rob(nums []int) int {
	if len(nums) == 1 {
		return nums[0]
	}
	return max(robLinear(nums[:len(nums)-1]), robLinear(nums[1:]))
}
