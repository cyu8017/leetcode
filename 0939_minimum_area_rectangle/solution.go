// LeetCode 0939 - Minimum Area Rectangle
// https://leetcode.com/problems/minimum-area-rectangle/

import "sort"

func minAreaRect(points [][]int) int {
	byX := map[int][]int{}
	for _, p := range points {
		byX[p[0]] = append(byX[p[0]], p[1])
	}
	xs := make([]int, 0, len(byX))
	for x := range byX {
		xs = append(xs, x)
	}
	sort.Ints(xs)
	last := map[[2]int]int{}
	ans := int(^uint(0) >> 1)
	found := false
	for _, x := range xs {
		ys := byX[x]
		sort.Ints(ys)
		for i := 0; i < len(ys); i++ {
			for j := i + 1; j < len(ys); j++ {
				y1, y2 := ys[i], ys[j]
				key := [2]int{y1, y2}
				if px, ok := last[key]; ok {
					area := (x - px) * (y2 - y1)
					if area < 0 {
						area = -area
					}
					if area < ans {
						ans = area
					}
					found = true
				}
				last[key] = x
			}
		}
	}
	if !found {
		return 0
	}
	return ans
}
