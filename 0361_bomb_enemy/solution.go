// LeetCode 0361 - Bomb Enemy
// https://leetcode.com/problems/bomb-enemy/

func maxKilledEnemies(grid [][]byte) int {
	if len(grid) == 0 || len(grid[0]) == 0 {
		return 0
	}

	rows := len(grid)
	cols := len(grid[0])
	rowHits := make([][]int, rows)
	colHits := make([][]int, rows)
	for row := 0; row < rows; row++ {
		rowHits[row] = make([]int, cols)
		colHits[row] = make([]int, cols)
	}

	for row := 0; row < rows; row++ {
		count := 0
		for col := 0; col < cols; col++ {
			switch grid[row][col] {
			case 'W':
				count = 0
			case 'E':
				count++
			default:
				rowHits[row][col] = count
			}
		}
		count = 0
		for col := cols - 1; col >= 0; col-- {
			switch grid[row][col] {
			case 'W':
				count = 0
			case 'E':
				count++
			default:
				rowHits[row][col] += count
			}
		}
	}

	for col := 0; col < cols; col++ {
		count := 0
		for row := 0; row < rows; row++ {
			switch grid[row][col] {
			case 'W':
				count = 0
			case 'E':
				count++
			default:
				colHits[row][col] = count
			}
		}
		count = 0
		for row := rows - 1; row >= 0; row-- {
			switch grid[row][col] {
			case 'W':
				count = 0
			case 'E':
				count++
			default:
				colHits[row][col] += count
			}
		}
	}

	result := 0
	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			total := rowHits[row][col] + colHits[row][col]
			if total > result {
				result = total
			}
		}
	}

	return result
}
