// LeetCode 0308 - Range Sum Query 2D - Mutable
// https://leetcode.com/problems/range-sum-query-2d-mutable/

type NumMatrix struct {
	matrix [][]int
	tree   [][]int
	rows   int
	cols   int
}

func Constructor(matrix [][]int) NumMatrix {
	rows := len(matrix)
	cols := 0
	if rows > 0 {
		cols = len(matrix[0])
	}
	obj := NumMatrix{
		matrix: matrix,
		tree:   make([][]int, rows+1),
		rows:   rows,
		cols:   cols,
	}
	for row := range obj.tree {
		obj.tree[row] = make([]int, cols+1)
	}
	add := func(row, col, delta int) {
		for rowIndex := row; rowIndex <= obj.rows; rowIndex += rowIndex & -rowIndex {
			for colIndex := col; colIndex <= obj.cols; colIndex += colIndex & -colIndex {
				obj.tree[rowIndex][colIndex] += delta
			}
		}
	}
	for row := 0; row < rows; row++ {
		for col := 0; col < cols; col++ {
			add(row+1, col+1, matrix[row][col])
		}
	}
	return obj
}

func (this *NumMatrix) Update(row int, col int, val int) {
	delta := val - this.matrix[row][col]
	this.matrix[row][col] = val
	for rowIndex := row + 1; rowIndex <= this.rows; rowIndex += rowIndex & -rowIndex {
		for colIndex := col + 1; colIndex <= this.cols; colIndex += colIndex & -colIndex {
			this.tree[rowIndex][colIndex] += delta
		}
	}
}

func (this *NumMatrix) SumRegion(row1 int, col1 int, row2 int, col2 int) int {
	prefix := func(row, col int) int {
		total := 0
		for rowIndex := row; rowIndex > 0; rowIndex -= rowIndex & -rowIndex {
			for colIndex := col; colIndex > 0; colIndex -= colIndex & -colIndex {
				total += this.tree[rowIndex][colIndex]
			}
		}
		return total
	}
	return prefix(row2+1, col2+1) - prefix(row1, col2+1) - prefix(row2+1, col1) + prefix(row1, col1)
}
