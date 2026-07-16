// LeetCode 0356 - Line Reflection
// https://leetcode.com/problems/line-reflection/

func isReflected(points [][]int) bool {
	pointSet := make(map[[2]int]bool, len(points))
	minX := points[0][0]
	maxX := points[0][0]

	for _, point := range points {
		if point[0] < minX {
			minX = point[0]
		}
		if point[0] > maxX {
			maxX = point[0]
		}
		pointSet[[2]int{point[0], point[1]}] = true
	}

	target := minX + maxX
	for _, point := range points {
		mirror := [2]int{target - point[0], point[1]}
		if !pointSet[mirror] {
			return false
		}
	}

	return true
}
