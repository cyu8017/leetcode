// LeetCode 2943 - Maximize Area of Square Hole in Grid
// https://leetcode.com/problems/maximize-area-of-square-hole-in-grid/

import "sort"

func maximizeSquareHoleArea(n int, m int, hBars []int, vBars []int) int {
	maxGap := func(bars []int, bound int) int {
		if len(bars) == 0 {
			return 1
		}
		sort.Ints(bars)
		best, cur := 1, 1
		for i := 1; i < len(bars); i++ {
			if bars[i] == bars[i-1]+1 {
				cur++
			} else {
				cur = 1
			}
			if cur > best {
				best = cur
			}
		}
		return best + 1
	}
	side := maxGap(hBars, n)
	vs := maxGap(vBars, m)
	if vs < side {
		side = vs
	}
	return side * side
}
