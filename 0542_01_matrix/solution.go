// LeetCode 0542 - 01 Matrix
// https://leetcode.com/problems/01-matrix/

func updateMatrix(mat [][]int) [][]int {
	rows := len(mat)
	cols := len(mat[0])
	const inf = 1_000_000_000
	dist := make([][]int, rows)
	type cell struct {
		row int
		col int
	}
	queue := make([]cell, 0)

	for row := 0; row < rows; row++ {
		dist[row] = make([]int, cols)
		for col := 0; col < cols; col++ {
			if mat[row][col] == 0 {
				dist[row][col] = 0
				queue = append(queue, cell{row, col})
			} else {
				dist[row][col] = inf
			}
		}
	}

	directions := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for head := 0; head < len(queue); head++ {
		current := queue[head]
		for _, direction := range directions {
			nextRow := current.row + direction[0]
			nextCol := current.col + direction[1]
			if nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols &&
				dist[nextRow][nextCol] > dist[current.row][current.col]+1 {
				dist[nextRow][nextCol] = dist[current.row][current.col] + 1
				queue = append(queue, cell{nextRow, nextCol})
			}
		}
	}

	return dist
}
