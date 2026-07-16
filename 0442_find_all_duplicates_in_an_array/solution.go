// LeetCode 0442 - Find All Duplicates in an Array
// https://leetcode.com/problems/find-all-duplicates-in-an-array/

func findDuplicates(nums []int) []int {
	result := make([]int, 0)
	for _, number := range nums {
		index := abs(number) - 1
		if nums[index] < 0 {
			result = append(result, abs(number))
		} else {
			nums[index] = -nums[index]
		}
	}
	return result
}

func abs(value int) int {
	if value < 0 {
		return -value
	}
	return value
}
