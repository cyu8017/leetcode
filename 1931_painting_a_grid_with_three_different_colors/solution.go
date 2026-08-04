// LeetCode 1931 - Painting a Grid With Three Different Colors
// https://leetcode.com/problems/painting-a-grid-with-three-different-colors/

func colorTheGrid(m int, n int) int {
	const MOD = 1000000007
	validColumn := func(mask int) bool {
		prev := -1
		for i := 0; i < m; i++ {
			c := mask % 3
			if c == prev {
				return false
			}
			prev = c
			mask /= 3
		}
		return true
	}
	getColors := func(mask int) []int {
		cols := make([]int, m)
		for i := 0; i < m; i++ {
			cols[i] = mask % 3
			mask /= 3
		}
		return cols
	}
	maxState := 1
	for i := 0; i < m; i++ {
		maxState *= 3
	}
	states := []int{}
	for s := 0; s < maxState; s++ {
		if validColumn(s) {
			states = append(states, s)
		}
	}
	compat := make(map[int][]int)
	for _, a := range states {
		ca := getColors(a)
		for _, b := range states {
			cb := getColors(b)
			ok := true
			for i := 0; i < m; i++ {
				if ca[i] == cb[i] {
					ok = false
					break
				}
			}
			if ok {
				compat[a] = append(compat[a], b)
			}
		}
	}
	memo := make(map[[2]int]int)
	var dp func(col, prev int) int
	dp = func(col, prev int) int {
		if col == n {
			return 1
		}
		key := [2]int{col, prev}
		if v, ok := memo[key]; ok {
			return v
		}
		total := 0
		cands := states
		if prev != -1 {
			cands = compat[prev]
		}
		for _, cur := range cands {
			total = (total + dp(col+1, cur)) % MOD
		}
		memo[key] = total
		return total
	}
	return dp(0, -1)
}
