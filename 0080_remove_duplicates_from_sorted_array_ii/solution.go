// LeetCode 0080 - Remove Duplicates from Sorted Array II
// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

func removeDuplicates(nums []int) int {
	if len(nums) <= 2 {
		return len(nums)
	}
	write := 2
	for i := 2; i < len(nums); i++ {
		if nums[i] != nums[write-2] {
			nums[write] = nums[i]
			write++
		}
	}
	return write
}
