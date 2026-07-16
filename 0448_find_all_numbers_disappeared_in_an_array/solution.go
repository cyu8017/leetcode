// LeetCode 0448 - Find All Numbers Disappeared in an Array
// https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/

func findDisappearedNumbers(nums []int) []int {
	for _, number := range nums {
		index := abs(number) - 1
		if nums[index] > 0 {
			nums[index] = -nums[index]
		}
	}

	result := make([]int, 0)
	for index, value := range nums {
		if value > 0 {
			result = append(result, index+1)
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
