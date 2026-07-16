// LeetCode 0317 - Shortest Distance from All Buildings
// https://leetcode.com/problems/shortest-distance-from-all-buildings/

func shortestDistance(grid [][]int) int {
	if len(grid) == 0 {
		return -1
	}

	rows := len(grid)
	cols := len(grid[0])
	buildings := 0
	distances := make([][]int, rows)
	reach := make([][]int, rows)
	for row := 0; row < rows; row++ {
		distances[row] = make([]int, cols)
		reach[row] = make([]int, cols)
		for col := 0; col < cols; col++ {
			if grid[row][col] == 1 {
				buildings++
			}
		}
	}

	directions := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			if grid[row][col] != 1 {
				continue
			}
			visited := make([][]bool, rows)
			for visitRow := 0; visitRow < rows; visitRow++ {
				visited[visitRow] = make([]bool, cols)
			}
			queue := [][3]int{{row, col, 0}}
			visited[row][col] = true
			for len(queue) > 0 {
				entry := queue[0]
				queue = queue[1:]
				currentRow, currentCol, distance := entry[0], entry[1], entry[2]
				for _, direction := range directions {
					nextRow := currentRow + direction[0]
					nextCol := currentCol + direction[1]
					if nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols &&
						grid[nextRow][nextCol] == 0 && !visited[nextRow][nextCol] {
						visited[nextRow][nextCol] = true
						distances[nextRow][nextCol] += distance + 1
						reach[nextRow][nextCol]++
						queue = append(queue, [3]int{nextRow, nextCol, distance + 1})
					}
				}
			}
		}
	}

	best := int(^uint(0) >> 1)
	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			if grid[row][col] == 0 && reach[row][col] == buildings && distances[row][col] < best {
				best = distances[row][col]
			}
		}
	}
	if best == int(^uint(0)>>1) {
		return -1
	}
	return best
}
