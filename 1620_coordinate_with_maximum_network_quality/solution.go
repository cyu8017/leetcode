// LeetCode 1620 - Coordinate With Maximum Network Quality
// https://leetcode.com/problems/coordinate-with-maximum-network-quality/

import "math"

func bestCoordinate(towers [][]int, radius int) []int {
	best := []int{0, 0}
	quality := -1
	for x := 0; x <= 50; x++ {
		for y := 0; y <= 50; y++ {
			q := 0
			for _, t := range towers {
				d := math.Hypot(float64(x-t[0]), float64(y-t[1]))
				if d <= float64(radius) {
					q += int(float64(t[2]) / (1 + d))
				}
			}
			if q > quality {
				quality = q
				best = []int{x, y}
			}
		}
	}
	return best
}
