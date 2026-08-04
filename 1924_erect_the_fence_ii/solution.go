// LeetCode 1924 - Erect the Fence II
// https://leetcode.com/problems/erect-the-fence-ii/

import "math"

func outerTrees(trees [][]int) []float64 {
	pts := make([][2]float64, len(trees))
	for i, p := range trees {
		pts[i] = [2]float64{float64(p[0]), float64(p[1])}
	}

	dist := func(a, b [2]float64) float64 {
		return math.Hypot(a[0]-b[0], a[1]-b[1])
	}
	circle2 := func(a, b [2]float64) ([2]float64, float64) {
		c := [2]float64{(a[0] + b[0]) / 2, (a[1] + b[1]) / 2}
		return c, dist(a, b) / 2
	}
	circle3 := func(a, b, c [2]float64) ([2]float64, float64) {
		ax, ay := a[0], a[1]
		bx, by := b[0], b[1]
		cx, cy := c[0], c[1]
		d := 2 * (ax*(by-cy) + bx*(cy-ay) + cx*(ay-by))
		if math.Abs(d) < 1e-12 {
			c1, r1 := circle2(a, b)
			c2, r2 := circle2(a, c)
			c3, r3 := circle2(b, c)
			bestC, bestR := c1, r1
			if r2 < bestR {
				bestC, bestR = c2, r2
			}
			if r3 < bestR {
				bestC, bestR = c3, r3
			}
			return bestC, bestR
		}
		ux := ((ax*ax+ay*ay)*(by-cy) + (bx*bx+by*by)*(cy-ay) + (cx*cx+cy*cy)*(ay-by)) / d
		uy := ((ax*ax+ay*ay)*(cx-bx) + (bx*bx+by*by)*(ax-cx) + (cx*cx+cy*cy)*(bx-ax)) / d
		center := [2]float64{ux, uy}
		return center, dist(center, a)
	}
	inside := func(center [2]float64, r float64, p [2]float64, valid bool) bool {
		if !valid {
			return false
		}
		return dist(center, p) <= r+1e-9
	}

	var center [2]float64
	var r float64
	valid := false
	for i, p := range pts {
		if !valid || !inside(center, r, p, valid) {
			center, r, valid = p, 0.0, true
			for j := 0; j < i; j++ {
				q := pts[j]
				if !inside(center, r, q, valid) {
					center, r = circle2(p, q)
					for k := 0; k < j; k++ {
						rr := pts[k]
						if !inside(center, r, rr, valid) {
							center, r = circle3(p, q, rr)
						}
					}
				}
			}
		}
	}
	return []float64{center[0], center[1], r}
}
