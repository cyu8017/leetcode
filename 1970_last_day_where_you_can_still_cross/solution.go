// LeetCode 1970 - Last Day Where You Can Still Cross
// https://leetcode.com/problems/last-day-where-you-can-still-cross/

func latestDayToCross(row int, col int, cells [][]int) int {
	can := func(day int) bool {
		blocked := make([][]bool, row)
		for i := range blocked {
			blocked[i] = make([]bool, col)
		}
		for i := 0; i < day; i++ {
			blocked[cells[i][0]-1][cells[i][1]-1] = true
		}
		stack := [][2]int{}
		seen := make([][]bool, row)
		for i := range seen {
			seen[i] = make([]bool, col)
		}
		for c := 0; c < col; c++ {
			if !blocked[0][c] {
				stack = append(stack, [2]int{0, c})
				seen[0][c] = true
			}
		}
		dirs := [][2]int{{-1, 0}, {1, 0}, {0, -1}, {0, 1}}
		for len(stack) > 0 {
			cur := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			r, c := cur[0], cur[1]
			if r == row-1 {
				return true
			}
			for _, d := range dirs {
				nr, nc := r+d[0], c+d[1]
				if nr >= 0 && nr < row && nc >= 0 && nc < col && !blocked[nr][nc] && !seen[nr][nc] {
					seen[nr][nc] = true
					stack = append(stack, [2]int{nr, nc})
				}
			}
		}
		return false
	}
	lo, hi, ans := 1, len(cells), 0
	for lo <= hi {
		mid := (lo + hi) / 2
		if can(mid) {
			ans = mid
			lo = mid + 1
		} else {
			hi = mid - 1
		}
	}
	return ans
}
