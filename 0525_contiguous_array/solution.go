// LeetCode 0525 - Contiguous Array
// https://leetcode.com/problems/contiguous-array/

func findMaxLength(nums []int) int {
	counts := map[int]int{0: -1}
	balance := 0
	best := 0

	for index, num := range nums {
		if num == 1 {
			balance++
		} else {
			balance--
		}
		if prev, ok := counts[balance]; ok {
			if index-prev > best {
				best = index - prev
			}
		} else {
			counts[balance] = index
		}
	}
	return best
}
