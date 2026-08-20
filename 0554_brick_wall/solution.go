// LeetCode 0554 - Brick Wall
// https://leetcode.com/problems/brick-wall/

func leastBricks(wall [][]int) int {
	edges := map[int]int{}
	for _, row := range wall {
		width := 0
		for _, brick := range row[:len(row)-1] {
			width += brick
			edges[width]++
		}
	}
	best := 0
	for _, count := range edges {
		if count > best {
			best = count
		}
	}
	return len(wall) - best
}
