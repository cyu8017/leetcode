// LeetCode 0027 - Remove Element
// https://leetcode.com/problems/remove-element/

func removeElement(nums []int, val int) int {
	write := 0
	for read := 0; read < len(nums); read++ {
		if nums[read] != val {
			nums[write] = nums[read]
			write++
		}
	}
	return write
}
