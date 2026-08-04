// LeetCode 1956 - Minimum Time For K Virus Variants to Spread
// https://leetcode.com/problems/minimum-time-for-k-virus-variants-to-spread/

import "sort"

func minDayskVariants(points [][]int, k int) int {
	ans := 1 << 30
	for x := 1; x <= 100; x++ {
		for y := 1; y <= 100; y++ {
			dists := make([]int, len(points))
			for i, p := range points {
				dx, dy := p[0]-x, p[1]-y
				if dx < 0 {
					dx = -dx
				}
				if dy < 0 {
					dy = -dy
				}
				dists[i] = dx + dy
			}
			sort.Ints(dists)
			if dists[k-1] < ans {
				ans = dists[k-1]
			}
		}
	}
	return ans
}
