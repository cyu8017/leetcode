// LeetCode 3484 - Design Spreadsheet
// https://leetcode.com/problems/design-spreadsheet/

import "strconv"
import "strings"

type Spreadsheet struct {
	cells map[string]int
}

func Constructor(rows int) Spreadsheet {
	return Spreadsheet{cells: map[string]int{}}
}

func (this *Spreadsheet) SetCell(cell string, value int) {
	this.cells[cell] = value
}

func (this *Spreadsheet) ResetCell(cell string) {
	delete(this.cells, cell)
}

func (this *Spreadsheet) GetValue(formula string) int {
	formula = strings.TrimPrefix(formula, "=")
	parts := strings.Split(formula, "+")
	sum := 0
	for _, p := range parts {
		if v, err := strconv.Atoi(p); err == nil {
			sum += v
		} else {
			sum += this.cells[p]
		}
	}
	return sum
}
