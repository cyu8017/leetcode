// LeetCode 0490 - The Maze
// https://leetcode.com/problems/the-maze/

func hasPath(maze [][]int, start []int, destination []int) bool {
	rows := len(maze)
	cols := len(maze[0])
	directions := [4][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
	visited := map[[2]int]bool{}
	stack := [][2]int{{start[0], start[1]}}

	for len(stack) > 0 {
		current := stack[len(stack)-1]
		stack = stack[:len(stack)-1]
		row, col := current[0], current[1]
		if visited[current] {
			continue
		}
		visited[current] = true
		if row == destination[0] && col == destination[1] {
			return true
		}
		for _, direction := range directions {
			nextRow, nextCol := row, col
			for nextRow+direction[0] >= 0 && nextRow+direction[0] < rows &&
				nextCol+direction[1] >= 0 && nextCol+direction[1] < cols &&
				maze[nextRow+direction[0]][nextCol+direction[1]] == 0 {
				nextRow += direction[0]
				nextCol += direction[1]
			}
			next := [2]int{nextRow, nextCol}
			if !visited[next] {
				stack = append(stack, next)
			}
		}
	}
	return false
}
