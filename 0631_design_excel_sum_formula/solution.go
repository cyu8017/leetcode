// LeetCode 0631 - Design Excel Sum Formula
// https://leetcode.com/problems/design-excel-sum-formula/

import (
	"strconv"
	"strings"
)

type Excel struct {
	height   int
	width    int
	values   [][]int
	formulas map[[2]int][][2]int
}

func Constructor(height int, width byte) Excel {
	w := int(width - 'A' + 1)
	values := make([][]int, height+1)
	for i := range values {
		values[i] = make([]int, w)
	}
	return Excel{height: height, width: w, values: values, formulas: map[[2]int][][2]int{}}
}

func (e *Excel) Set(row int, column byte, val int) {
	col := int(column - 'A')
	delete(e.formulas, [2]int{row, col})
	e.values[row][col] = val
}

func (e *Excel) Get(row int, column byte) int {
	return e.eval(row, int(column-'A'))
}

func (e *Excel) Sum(row int, column byte, numbers []string) int {
	col := int(column - 'A')
	cells := [][2]int{}
	for _, token := range numbers {
		if strings.Contains(token, ":") {
			parts := strings.Split(token, ":")
			r1, c1 := e.parse(parts[0])
			r2, c2 := e.parse(parts[1])
			for r := r1; r <= r2; r++ {
				for c := c1; c <= c2; c++ {
					cells = append(cells, [2]int{r, c})
				}
			}
		} else {
			cells = append(cells, e.parse(token))
		}
	}
	e.formulas[[2]int{row, col}] = cells
	return e.eval(row, col)
}

func (e *Excel) parse(cell string) [2]int {
	row, _ := strconv.Atoi(cell[1:])
	return [2]int{row, int(cell[0] - 'A')}
}

func (e *Excel) eval(row, col int) int {
	if cells, ok := e.formulas[[2]int{row, col}]; ok {
		total := 0
		for _, cell := range cells {
			total += e.eval(cell[0], cell[1])
		}
		return total
	}
	return e.values[row][col]
}
