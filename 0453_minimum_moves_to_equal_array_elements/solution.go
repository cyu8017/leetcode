// LeetCode 0453 - Minimum Moves to Equal Array Elements
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements/

func minMoves(nums []int) int {
	minimum := nums[0]
	for _, value := range nums[1:] {
		if value < minimum {
			minimum = value
		}
	}

	total := 0
	for _, value := range nums {
		total += value - minimum
	}
	return total
}
