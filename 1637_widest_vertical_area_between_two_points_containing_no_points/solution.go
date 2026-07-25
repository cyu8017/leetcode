// LeetCode 1637 - Widest Vertical Area Between Two Points Containing No Points
// https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

import "sort"

func maxWidthOfVerticalArea(points [][]int) int {
	xs := make([]int, len(points))
	for i, p := range points {
		xs[i] = p[0]
	}
	sort.Ints(xs)
	ans := 0
	for i := 1; i < len(xs); i++ {
		if xs[i]-xs[i-1] > ans {
			ans = xs[i] - xs[i-1]
		}
	}
	return ans
}
