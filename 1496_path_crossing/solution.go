// LeetCode 1496 - Path Crossing
// https://leetcode.com/problems/path-crossing/

func isPathCrossing(path string) bool {
	x, y := 0, 0
	seen := map[[2]int]bool{{0, 0}: true}
	move := map[byte][2]int{'N': {0, 1}, 'S': {0, -1}, 'E': {1, 0}, 'W': {-1, 0}}
	for i := 0; i < len(path); i++ {
		d := move[path[i]]
		x += d[0]
		y += d[1]
		if seen[[2]int{x, y}] {
			return true
		}
		seen[[2]int{x, y}] = true
	}
	return false
}
