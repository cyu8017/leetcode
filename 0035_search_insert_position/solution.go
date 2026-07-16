// LeetCode 0035 - Search Insert Position
// https://leetcode.com/problems/search-insert-position/

func searchInsert(nums []int, target int) int {
	left := 0
	right := len(nums)

	for left < right {
		mid := (left + right) / 2
		if nums[mid] < target {
			left = mid + 1
		} else {
			right = mid
		}
	}

	return left
}
