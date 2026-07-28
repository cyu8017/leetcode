// LeetCode 1036 - Escape a Large Maze
// https://leetcode.com/problems/escape-a-large-maze/

func isEscapePossible(blocked [][]int, source []int, target []int) bool {
	blockedSet := map[[2]int]bool{}
	for _, b := range blocked {
		blockedSet[[2]int{b[0], b[1]}] = true
	}
	b := len(blocked)
	limit := b * (b - 1) / 2
	bfs := func(start, goal []int) bool {
		q := [][2]int{{start[0], start[1]}}
		seen := map[[2]int]bool{[2]int{start[0], start[1]}: true}
		dirs := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
		for len(q) > 0 {
			if len(seen) > limit {
				return true
			}
			cur := q[0]
			q = q[1:]
			r, c := cur[0], cur[1]
			if r == goal[0] && c == goal[1] {
				return true
			}
			for _, d := range dirs {
				nr, nc := r+d[0], c+d[1]
				key := [2]int{nr, nc}
				if nr >= 0 && nr < 1000000 && nc >= 0 && nc < 1000000 && !blockedSet[key] && !seen[key] {
					seen[key] = true
					q = append(q, key)
				}
			}
		}
		return false
	}
	return bfs(source, target) && bfs(target, source)
}
