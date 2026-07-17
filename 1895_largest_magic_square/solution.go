// LeetCode 1895 - Largest Magic Square
// https://leetcode.com/problems/largest-magic-square/

func largestMagicSquare(grid [][]int) int {
	rows := len(grid)
	cols := len(grid[0])
	rowPrefix := make([][]int, rows)
	colPrefix := make([][]int, cols)
	for i := range rowPrefix {
		rowPrefix[i] = make([]int, cols+1)
	}
	for j := range colPrefix {
		colPrefix[j] = make([]int, rows+1)
	}

	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			rowPrefix[i][j+1] = rowPrefix[i][j] + grid[i][j]
			colPrefix[j][i+1] = colPrefix[j][i] + grid[i][j]
		}
	}

	rowSum := func(row int, colStart int, colEnd int) int {
		return rowPrefix[row][colEnd+1] - rowPrefix[row][colStart]
	}
	colSum := func(col int, rowStart int, rowEnd int) int {
		return colPrefix[col][rowEnd+1] - colPrefix[col][rowStart]
	}
	isMagic := func(rowStart int, colStart int, size int) bool {
		target := rowSum(rowStart, colStart, colStart+size-1)
		for row := rowStart; row < rowStart+size; row++ {
			if rowSum(row, colStart, colStart+size-1) != target {
				return false
			}
		}
		for col := colStart; col < colStart+size; col++ {
			if colSum(col, rowStart, rowStart+size-1) != target {
				return false
			}
		}
		diag1 := 0
		diag2 := 0
		for offset := 0; offset < size; offset++ {
			diag1 += grid[rowStart+offset][colStart+offset]
			diag2 += grid[rowStart+offset][colStart+size-1-offset]
		}
		return diag1 == target && diag2 == target
	}

	limit := rows
	if cols < limit {
		limit = cols
	}
	for size := limit; size >= 1; size-- {
		for rowStart := 0; rowStart <= rows-size; rowStart++ {
			for colStart := 0; colStart <= cols-size; colStart++ {
				if isMagic(rowStart, colStart, size) {
					return size
				}
			}
		}
	}
	return 1
}
