// LeetCode 1610 - Maximum Number of Visible Points
// https://leetcode.com/problems/maximum-number-of-visible-points/

import (
	"math"
	"sort"
)

func visiblePoints(points [][]int, angle int, location []int) int {
	same := 0
	a := []float64{}
	for _, p := range points {
		dx := float64(p[0] - location[0])
		dy := float64(p[1] - location[1])
		if dx == 0 && dy == 0 {
			same++
		} else {
			a = append(a, math.Atan2(dy, dx))
		}
	}
	sort.Float64s(a)
	ext := append([]float64{}, a...)
	for _, x := range a {
		ext = append(ext, x+2*math.Pi)
	}
	width := float64(angle)*math.Pi/180 + 1e-12
	left, best := 0, 0
	for right, value := range ext {
		for value-ext[left] > width {
			left++
		}
		cur := right - left + 1
		if cur > len(a) {
			cur = len(a)
		}
		if cur > best {
			best = cur
		}
	}
	return best + same
}
