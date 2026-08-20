// LeetCode 3736 - Minimum Moves to Equal Array Elements III
// https://leetcode.com/problems/minimum-moves-to-equal-array-elements-iii/

func minMoves(nums []int) int {
	mx, s := 0, 0
	for _, x := range nums {
		mx = max(mx, x)
		s += x
	}
	return mx*len(nums) - s
}
