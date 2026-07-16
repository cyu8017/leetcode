// LeetCode 0075 - Sort Colors
// https://leetcode.com/problems/sort-colors/

func sortColors(nums []int) {
	low := 0
	mid := 0
	high := len(nums) - 1

	for mid <= high {
		switch nums[mid] {
		case 0:
			nums[low], nums[mid] = nums[mid], nums[low]
			low++
			mid++
		case 1:
			mid++
		default:
			nums[mid], nums[high] = nums[high], nums[mid]
			high--
		}
	}
}
