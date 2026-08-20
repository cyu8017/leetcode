// LeetCode 0812 - Largest Triangle Area
// https://leetcode.com/problems/largest-triangle-area/

func largestTriangleArea(points [][]int) float64 {
	best := 0.0
	n := len(points)
	for i := 0; i < n; i++ {
		x1, y1 := points[i][0], points[i][1]
		for j := i + 1; j < n; j++ {
			x2, y2 := points[j][0], points[j][1]
			for k := j + 1; k < n; k++ {
				x3, y3 := points[k][0], points[k][1]
				area := float64(abs(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))) / 2.0
				if area > best {
					best = area
				}
			}
		}
	}
	return best
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}
