// LeetCode 2250 - Count Number of Rectangles Containing Each Point
// https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

import "sort"

func countRectangles(rectangles [][]int, points [][]int) []int {
	byH := make([][]int, 101)
	for _, r := range rectangles {
		byH[r[1]] = append(byH[r[1]], r[0])
	}
	for h := 1; h <= 100; h++ {
		sort.Ints(byH[h])
	}
	ans := make([]int, len(points))
	for i, p := range points {
		x, y := p[0], p[1]
		cnt := 0
		for h := y; h <= 100; h++ {
			xs := byH[h]
			j := sort.Search(len(xs), func(j int) bool { return xs[j] >= x })
			cnt += len(xs) - j
		}
		ans[i] = cnt
	}
	return ans
}
