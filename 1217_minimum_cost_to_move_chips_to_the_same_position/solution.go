// LeetCode 1217 - Minimum Cost to Move Chips to The Same Position
// https://leetcode.com/problems/minimum-cost-to-move-chips-to-the-same-position/

func minCostToMoveChips(position []int) int {
	odd := 0
	for _, x := range position {
		odd += x & 1
	}
	even := len(position) - odd
	if odd < even {
		return odd
	}
	return even
}
