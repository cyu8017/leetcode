// LeetCode 1828 - Queries on Number of Points Inside a Circle
// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

func countPoints(points [][]int, queries [][]int) []int {
	result := make([]int, 0, len(queries))
	for _, query := range queries {
		xq, yq, r := query[0], query[1], query[2]
		radiusSq := r * r
		count := 0
		for _, point := range points {
			x, y := point[0], point[1]
			dx := x - xq
			dy := y - yq
			if dx*dx+dy*dy <= radiusSq {
				count++
			}
		}
		result = append(result, count)
	}
	return result
}
