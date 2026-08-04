// LeetCode 1515 - Best Position for a Service Centre
// https://leetcode.com/problems/best-position-for-a-service-centre/

import "math"

func getMinDistSum(positions [][]int) float64 {
	x, y := 0.0, 0.0
	for _, p := range positions {
		x += float64(p[0])
		y += float64(p[1])
	}
	n := float64(len(positions))
	x /= n
	y /= n
	distance := func(a, b float64) float64 {
		sum := 0.0
		for _, p := range positions {
			sum += math.Hypot(a-float64(p[0]), b-float64(p[1]))
		}
		return sum
	}
	for i := 0; i < 10000; i++ {
		numX, numY, den := 0.0, 0.0, 0.0
		var cx, cy float64
		coincident := false
		for _, p := range positions {
			d := math.Hypot(x-float64(p[0]), y-float64(p[1]))
			if d < 1e-12 {
				cx, cy = float64(p[0]), float64(p[1])
				coincident = true
				break
			}
			numX += float64(p[0]) / d
			numY += float64(p[1]) / d
			den += 1 / d
		}
		nx, ny := numX/den, numY/den
		if coincident {
			nx, ny = cx, cy
		}
		if math.Hypot(nx-x, ny-y) < 1e-8 {
			x, y = nx, ny
			break
		}
		x, y = nx, ny
	}
	return distance(x, y)
}
