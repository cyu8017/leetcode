// LeetCode 0573 - Squirrel Simulation
// https://leetcode.com/problems/squirrel-simulation/

func minDistance(height int, width int, tree []int, squirrel []int, nuts [][]int) int {
	dist := func(a, b []int) int {
		d0 := a[0] - b[0]
		if d0 < 0 {
			d0 = -d0
		}
		d1 := a[1] - b[1]
		if d1 < 0 {
			d1 = -d1
		}
		return d0 + d1
	}
	total := 0
	bestSave := 0
	for i, nut := range nuts {
		total += 2 * dist(tree, nut)
		save := dist(tree, nut) - dist(squirrel, nut)
		if i == 0 || save > bestSave {
			bestSave = save
		}
	}
	_ = height
	_ = width
	return total - bestSave
}
