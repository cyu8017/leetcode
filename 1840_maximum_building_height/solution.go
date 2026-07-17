// LeetCode 1840 - Maximum Building Height
// https://leetcode.com/problems/maximum-building-height/

import "sort"

func maxBuilding(n int, restrictions [][]int) int {
	points := make([][]int, 0, len(restrictions)+2)
	points = append(points, []int{1, 0})
	points = append(points, restrictions...)
	sort.Slice(points, func(i, j int) bool {
		return points[i][0] < points[j][0]
	})
	if points[len(points)-1][0] != n {
		points = append(points, []int{n, n - 1})
	}

	for i := 1; i < len(points); i++ {
		prevID, prevHeight := points[i-1][0], points[i-1][1]
		currID, currHeight := points[i][0], points[i][1]
		points[i][1] = min(currHeight, prevHeight+currID-prevID)
	}
	for i := len(points) - 2; i >= 0; i-- {
		nextID, nextHeight := points[i+1][0], points[i+1][1]
		currID, currHeight := points[i][0], points[i][1]
		points[i][1] = min(currHeight, nextHeight+nextID-currID)
	}

	best := 0
	for _, point := range points {
		if point[1] > best {
			best = point[1]
		}
	}
	for i := 0; i < len(points)-1; i++ {
		id1, h1 := points[i][0], points[i][1]
		id2, h2 := points[i+1][0], points[i+1][1]
		candidate := (h1 + h2 + id2 - id1) / 2
		if candidate > best {
			best = candidate
		}
	}
	return best
}
