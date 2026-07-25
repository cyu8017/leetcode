// LeetCode 1659 - Maximize Grid Happiness
// https://leetcode.com/problems/maximize-grid-happiness/

func getMaxGridHappiness(m, n, introvertsCount, extrovertsCount int) int {
	states := 1
	for i := 0; i < n; i++ {
		states *= 3
	}
	cells := make([][]int, states)
	intro := make([]int, states)
	extro := make([]int, states)
	row := make([]int, states)
	for s := 0; s < states; s++ {
		cells[s] = make([]int, n)
		x := s
		for j := 0; j < n; j++ {
			cells[s][j] = x % 3
			x /= 3
		}
		val := 0
		for j := 0; j < n; j++ {
			z := cells[s][j]
			if z == 1 {
				intro[s]++
				val += 120
			} else if z == 2 {
				extro[s]++
				val += 40
			}
		}
		for j := 1; j < n; j++ {
			val += pairCost1659(cells[s][j-1], cells[s][j])
		}
		row[s] = val
	}
	compat := make([][]int, states)
	for a := 0; a < states; a++ {
		compat[a] = make([]int, states)
		for b := 0; b < states; b++ {
			v := 0
			for j := 0; j < n; j++ {
				v += pairCost1659(cells[a][j], cells[b][j])
			}
			compat[a][b] = v
		}
	}
	memo := make([]int, (m+1)*states*(introvertsCount+1)*(extrovertsCount+1))
	seen := make([]bool, len(memo))
	var dfs func(r, prev, i, e int) int
	dfs = func(r, prev, i, e int) int {
		if r == m {
			return 0
		}
		id := (((r*states+prev)*(introvertsCount+1) + i) * (extrovertsCount + 1)) + e
		if seen[id] {
			return memo[id]
		}
		best := 0
		for s := 0; s < states; s++ {
			if intro[s] > i || extro[s] > e {
				continue
			}
			val := row[s] + compat[prev][s] + dfs(r+1, s, i-intro[s], e-extro[s])
			if val > best {
				best = val
			}
		}
		seen[id] = true
		memo[id] = best
		return best
	}
	return dfs(0, 0, introvertsCount, extrovertsCount)
}

func pairCost1659(a, b int) int {
	if a == 0 || b == 0 {
		return 0
	}
	va, vb := 20, 20
	if a == 1 {
		va = -30
	}
	if b == 1 {
		vb = -30
	}
	return va + vb
}
