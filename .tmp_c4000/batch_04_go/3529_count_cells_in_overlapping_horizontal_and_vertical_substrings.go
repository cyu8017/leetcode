// LeetCode 3529 - Count Cells in Overlapping Horizontal and Vertical Substrings
// https://leetcode.com/problems/count-cells-in-overlapping-horizontal-and-vertical-substrings/

func countCells(grid [][]byte, pattern string) int {
	m := len(grid)
	n := len(grid[0])
	row := make([]byte, 0, m*n)
	col := make([]byte, 0, m*n)
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			row = append(row, grid[i][j])
		}
	}
	for j := 0; j < n; j++ {
		for i := 0; i < m; i++ {
			col = append(col, grid[i][j])
		}
	}
	hMark := make([][]bool, m)
	vMark := make([][]bool, m)
	for i := 0; i < m; i++ {
		hMark[i] = make([]bool, n)
		vMark[i] = make([]bool, n)
	}
	p := []byte(pattern)
	for i := 0; i+len(p) <= len(row); i++ {
		ok := true
		for t := 0; t < len(p); t++ {
			if row[i+t] != p[t] {
				ok = false
				break
			}
		}
		if ok {
			for t := 0; t < len(p); t++ {
				pos := i + t
				hMark[pos/n][pos%n] = true
			}
		}
	}
	for i := 0; i+len(p) <= len(col); i++ {
		ok := true
		for t := 0; t < len(p); t++ {
			if col[i+t] != p[t] {
				ok = false
				break
			}
		}
		if ok {
			for t := 0; t < len(p); t++ {
				pos := i + t
				vMark[pos%m][pos/m] = true
			}
		}
	}
	ans := 0
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if hMark[i][j] && vMark[i][j] {
				ans++
			}
		}
	}
	return ans
}
