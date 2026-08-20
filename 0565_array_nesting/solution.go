// LeetCode 0565 - Array Nesting
// https://leetcode.com/problems/array-nesting/

func arrayNesting(nums []int) int {
	best := 0
	for i := range nums {
		if nums[i] < 0 {
			continue
		}
		length := 0
		j := i
		for nums[j] >= 0 {
			nxt := nums[j]
			nums[j] = -1
			j = nxt
			length++
		}
		if length > best {
			best = length
		}
	}
	return best
}
