// LeetCode 0026 - Remove Duplicates from Sorted Array
// https://leetcode.com/problems/remove-duplicates-from-sorted-array/

func removeDuplicates(nums []int) int {
	if len(nums) == 0 {
		return 0
	}
	write := 1
	for read := 1; read < len(nums); read++ {
		if nums[read] != nums[write-1] {
			nums[write] = nums[read]
			write++
		}
	}
	return write
}
