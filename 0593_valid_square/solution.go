// LeetCode 0593 - Valid Square
// https://leetcode.com/problems/valid-square/

import "sort"

func validSquare(p1 []int, p2 []int, p3 []int, p4 []int) bool {
	dist := func(a, b []int) int {
		return (a[0]-b[0])*(a[0]-b[0]) + (a[1]-b[1])*(a[1]-b[1])
	}
	points := [][]int{p1, p2, p3, p4}
	distances := []int{}
	for i := 0; i < 4; i++ {
		for j := i + 1; j < 4; j++ {
			distances = append(distances, dist(points[i], points[j]))
		}
	}
	sort.Ints(distances)
	return distances[0] > 0 &&
		distances[0] == distances[1] && distances[1] == distances[2] && distances[2] == distances[3] &&
		distances[4] == distances[5] &&
		distances[4] == 2*distances[0]
}
