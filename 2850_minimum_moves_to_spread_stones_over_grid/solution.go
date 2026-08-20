// LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
// https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

func minimumMoves(grid [][]int) int {
	var extras, zeros [][2]int
	for i := 0; i < 3; i++ {
		for j := 0; j < 3; j++ {
			if grid[i][j] == 0 {
				zeros = append(zeros, [2]int{i, j})
			} else if grid[i][j] > 1 {
				for k := 0; k < grid[i][j]-1; k++ {
					extras = append(extras, [2]int{i, j})
				}
			}
		}
	}
	if len(zeros) == 0 {
		return 0
	}
	abs := func(x int) int {
		if x < 0 {
			return -x
		}
		return x
	}
	best := 1 << 30
	var dfs func(int, int)
	dfs = func(i, cost int) {
		if cost >= best {
			return
		}
		if i == len(zeros) {
			best = cost
			return
		}
		for j := 0; j < len(extras); j++ {
			if extras[j][0] < 0 {
				continue
			}
			e := extras[j]
			extras[j][0] = -1
			d := abs(e[0]-zeros[i][0]) + abs(e[1]-zeros[i][1])
			dfs(i+1, cost+d)
			extras[j] = e
		}
	}
	dfs(0, 0)
	return best
}
