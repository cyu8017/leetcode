// LeetCode 2936 - Number of Equal Numbers Blocks
// https://leetcode.com/problems/number-of-equal-numbers-blocks/

func blockCount(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	ans := 1
	for i := 1; i < len(nums); i++ {
		if nums[i] != nums[i-1] {
			ans++
		}
	}
	return ans
}
