// LeetCode 1453 - Maximum Number of Darts Inside of a Circular Dartboard
// https://leetcode.com/problems/maximum-number-of-darts-inside-of-a-circular-dartboard/

import "math"

func numPoints(darts [][]int, r int) int {
	ans := 0
	if len(darts) > 0 {
		ans = 1
	}
	rr := float64(r)
	for i, p1 := range darts {
		x1, y1 := float64(p1[0]), float64(p1[1])
		for _, p2 := range darts[i+1:] {
			x2, y2 := float64(p2[0]), float64(p2[1])
			dx, dy := x2-x1, y2-y1
			d2 := dx*dx + dy*dy
			if d2 > 4*rr*rr || d2 == 0 {
				continue
			}
			d := math.Sqrt(d2)
			h := math.Sqrt(rr*rr - d2/4)
			mx, my := (x1+x2)/2, (y1+y2)/2
			for _, sign := range []float64{-1, 1} {
				cx := mx + sign*(-dy)*h/d
				cy := my + sign*dx*h/d
				count := 0
				for _, p := range darts {
					x, y := float64(p[0]), float64(p[1])
					if (x-cx)*(x-cx)+(y-cy)*(y-cy) <= rr*rr+1e-7 {
						count++
					}
				}
				if count > ans {
					ans = count
				}
			}
		}
	}
	return ans
}
