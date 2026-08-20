// LeetCode 0587 - Erect the Fence
// https://leetcode.com/problems/erect-the-fence/

import "sort"

func outerTrees(trees [][]int) [][]int {
	points := make([][2]int, len(trees))
	for i, t := range trees {
		points[i] = [2]int{t[0], t[1]}
	}
	sort.Slice(points, func(i, j int) bool {
		if points[i][0] == points[j][0] {
			return points[i][1] < points[j][1]
		}
		return points[i][0] < points[j][0]
	})
	if len(points) <= 1 {
		out := make([][]int, len(points))
		for i, p := range points {
			out[i] = []int{p[0], p[1]}
		}
		return out
	}
	cross := func(o, a, b [2]int) int {
		return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])
	}
	build := func(ordered [][2]int) [][2]int {
		hull := [][2]int{}
		for _, point := range ordered {
			for len(hull) >= 2 && cross(hull[len(hull)-2], hull[len(hull)-1], point) < 0 {
				hull = hull[:len(hull)-1]
			}
			hull = append(hull, point)
		}
		return hull
	}
	lower := build(points)
	rev := make([][2]int, len(points))
	for i := range points {
		rev[i] = points[len(points)-1-i]
	}
	upper := build(rev)
	seen := map[[2]int]struct{}{}
	hull := [][2]int{}
	for _, p := range append(lower[:len(lower)-1], upper[:len(upper)-1]...) {
		if _, ok := seen[p]; ok {
			continue
		}
		seen[p] = struct{}{}
		hull = append(hull, p)
	}
	out := make([][]int, len(hull))
	for i, p := range hull {
		out[i] = []int{p[0], p[1]}
	}
	return out
}
