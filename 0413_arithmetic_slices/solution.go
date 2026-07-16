// LeetCode 0413 - Arithmetic Slices
// https://leetcode.com/problems/arithmetic-slices/

func numberOfArithmeticSlices(nums []int) int {
	if len(nums) < 3 {
		return 0
	}

	total := 0
	current := 0
	for index := 2; index < len(nums); index++ {
		if nums[index]-nums[index-1] == nums[index-1]-nums[index-2] {
			current++
			total += current
		} else {
			current = 0
		}
	}
	return total
}
