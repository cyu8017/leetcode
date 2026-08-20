// LeetCode 0912 - Sort an Array
// https://leetcode.com/problems/sort-an-array/

func sortArray(nums []int) []int {
	if len(nums) <= 1 {
		return nums
	}
	mid := len(nums) / 2
	left := sortArray(append([]int{}, nums[:mid]...))
	right := sortArray(append([]int{}, nums[mid:]...))
	merged := make([]int, 0, len(nums))
	i, j := 0, 0
	for i < len(left) && j < len(right) {
		if left[i] <= right[j] {
			merged = append(merged, left[i])
			i++
		} else {
			merged = append(merged, right[j])
			j++
		}
	}
	merged = append(merged, left[i:]...)
	merged = append(merged, right[j:]...)
	return merged
}
