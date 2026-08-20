// LeetCode 2087 - Minimum Cost Homecoming of a Robot in a Grid
// https://leetcode.com/problems/minimum-cost-homecoming-of-a-robot-in-a-grid/

func minCost(startPos []int, homePos []int, rowCosts []int, colCosts []int) int {
	ans := 0
	sr, sc := startPos[0], startPos[1]
	hr, hc := homePos[0], homePos[1]
	if sr < hr {
		for r := sr + 1; r <= hr; r++ {
			ans += rowCosts[r]
		}
	} else {
		for r := sr - 1; r >= hr; r-- {
			ans += rowCosts[r]
		}
	}
	if sc < hc {
		for c := sc + 1; c <= hc; c++ {
			ans += colCosts[c]
		}
	} else {
		for c := sc - 1; c >= hc; c-- {
			ans += colCosts[c]
		}
	}
	return ans
}
