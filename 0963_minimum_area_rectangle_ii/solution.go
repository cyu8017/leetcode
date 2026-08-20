// LeetCode 0963 - Minimum Area Rectangle II
// https://leetcode.com/problems/minimum-area-rectangle-ii/

import "math"

func minAreaFreeRect(points [][]int) float64 {
	type pt struct{ x, y float64 }
	n := len(points)
	pts := make([]pt, n)
	for i, p := range points {
		pts[i] = pt{float64(p[0]), float64(p[1])}
	}
	type key struct {
		cx, cy, dist float64
	}
	groups := map[key][][2]pt{}
	for i := 0; i < n; i++ {
		for j := i + 1; j < n; j++ {
			p, q := pts[i], pts[j]
			cx := (p.x + q.x) / 2
			cy := (p.y + q.y) / 2
			dx, dy := p.x-q.x, p.y-q.y
			dist := dx*dx + dy*dy
			k := key{cx, cy, dist}
			groups[k] = append(groups[k], [2]pt{p, q})
		}
	}
	ans := math.Inf(1)
	for _, pairs := range groups {
		for i := 0; i < len(pairs); i++ {
			for j := i + 1; j < len(pairs); j++ {
				p1, p2, q2 := pairs[i][0], pairs[j][0], pairs[j][1]
				d1x, d1y := p1.x-p2.x, p1.y-p2.y
				d2x, d2y := p1.x-q2.x, p1.y-q2.y
				area := math.Hypot(d1x, d1y) * math.Hypot(d2x, d2y)
				if area > 0 && area < ans {
					ans = area
				}
			}
		}
	}
	if math.IsInf(ans, 1) {
		return 0
	}
	return ans
}
