// LeetCode 0699 - Falling Squares
// https://leetcode.com/problems/falling-squares/

func fallingSquares(positions [][]int) []int {
	type interval struct{ left, right, height int }
	intervals := []interval{}
	answer := []int{}
	maxHeight := 0
	for _, pos := range positions {
		left, side := pos[0], pos[1]
		right := left + side
		base := 0
		for _, iv := range intervals {
			if iv.right > left && iv.left < right && iv.height > base {
				base = iv.height
			}
		}
		height := base + side
		intervals = append(intervals, interval{left, right, height})
		if height > maxHeight {
			maxHeight = height
		}
		answer = append(answer, maxHeight)
	}
	return answer
}
