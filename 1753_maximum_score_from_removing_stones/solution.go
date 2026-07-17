// LeetCode 1753 - Maximum Score From Removing Stones
// https://leetcode.com/problems/maximum-score-from-removing-stones/

import "sort"

func maximumScore(a int, b int, c int) int {
	stones := []int{a, b, c}
	sort.Sort(sort.Reverse(sort.IntSlice(stones)))
	score := 0
	for stones[0] > 0 && stones[1] > 0 {
		stones[0]--
		stones[1]--
		score++
		sort.Sort(sort.Reverse(sort.IntSlice(stones)))
	}
	return score
}
