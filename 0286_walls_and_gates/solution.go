// LeetCode 0286 - Walls and Gates
// https://leetcode.com/problems/walls-and-gates/

import "math"

func wallsAndGates(rooms [][]int) {
	if len(rooms) == 0 || len(rooms[0]) == 0 {
		return
	}

	rows, cols := len(rooms), len(rooms[0])
	queue := make([][2]int, 0)

	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			if rooms[row][col] == 0 {
				queue = append(queue, [2]int{row, col})
			}
		}
	}

	directions := [][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	for len(queue) > 0 {
		current := queue[0]
		queue = queue[1:]
		for _, direction := range directions {
			nextRow := current[0] + direction[0]
			nextCol := current[1] + direction[1]
			if nextRow >= 0 && nextRow < rows && nextCol >= 0 && nextCol < cols &&
				rooms[nextRow][nextCol] == math.MaxInt32 {
				rooms[nextRow][nextCol] = rooms[current[0]][current[1]] + 1
				queue = append(queue, [2]int{nextRow, nextCol})
			}
		}
	}
}
