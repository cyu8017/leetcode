// LeetCode 1728 - Cat and Mouse II
// https://leetcode.com/problems/cat-and-mouse-ii/

func canMouseWin(grid []string, catJump int, mouseJump int) bool {
	rows, cols := len(grid), len(grid[0])
	totalOpen := 0
	mouse, cat, food := 0, 0, 0
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			cell := grid[r][c]
			if cell != '#' {
				totalOpen++
			}
			switch cell {
			case 'M':
				mouse = r*cols + c
			case 'C':
				cat = r*cols + c
			case 'F':
				food = r*cols + c
			}
		}
	}
	dirs := [4][2]int{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}
	computeMoves := func(pos, jump int) []int {
		r, c := pos/cols, pos%cols
		out := []int{pos}
		for _, dir := range dirs {
			for step := 1; step <= jump; step++ {
				nr, nc := r+dir[0]*step, c+dir[1]*step
				if nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr][nc] == '#' {
					break
				}
				out = append(out, nr*cols+nc)
			}
		}
		return out
	}
	cells := rows * cols
	mouseMoves := make([][]int, cells)
	catMoves := make([][]int, cells)
	for r := 0; r < rows; r++ {
		for c := 0; c < cols; c++ {
			if grid[r][c] != '#' {
				pos := r*cols + c
				mouseMoves[pos] = computeMoves(pos, mouseJump)
				catMoves[pos] = computeMoves(pos, catJump)
			}
		}
	}
	maxTurn := 2 * totalOpen
	memo := make([]int8, cells*cells*maxTurn)
	var win func(m, c, turn int) bool
	win = func(m, c, turn int) bool {
		if turn >= maxTurn {
			return false
		}
		if m == food {
			return true
		}
		if c == food || c == m {
			return false
		}
		key := (m*cells+c)*maxTurn + turn
		if memo[key] != 0 {
			return memo[key] == 1
		}
		var result bool
		if turn%2 == 0 {
			for _, nm := range mouseMoves[m] {
				if win(nm, c, turn+1) {
					result = true
					break
				}
			}
		} else {
			result = true
			for _, nc := range catMoves[c] {
				if !win(m, nc, turn+1) {
					result = false
					break
				}
			}
		}
		if result {
			memo[key] = 1
		} else {
			memo[key] = 2
		}
		return result
	}
	return win(mouse, cat, 0)
}
