// LeetCode 1001 - Grid Illumination
// https://leetcode.com/problems/grid-illumination/

func gridIllumination(n int, lamps [][]int, queries [][]int) []int {
	rows := map[int]int{}
	cols := map[int]int{}
	diag1 := map[int]int{}
	diag2 := map[int]int{}
	lit := map[[2]int]bool{}
	for _, lamp := range lamps {
		r, c := lamp[0], lamp[1]
		key := [2]int{r, c}
		if lit[key] {
			continue
		}
		lit[key] = true
		rows[r]++
		cols[c]++
		diag1[r-c]++
		diag2[r+c]++
	}
	ans := make([]int, len(queries))
	for qi, q := range queries {
		r, c := q[0], q[1]
		if rows[r] > 0 || cols[c] > 0 || diag1[r-c] > 0 || diag2[r+c] > 0 {
			ans[qi] = 1
		}
		for i := r - 1; i <= r+1; i++ {
			for j := c - 1; j <= c+1; j++ {
				key := [2]int{i, j}
				if lit[key] {
					delete(lit, key)
					rows[i]--
					cols[j]--
					diag1[i-j]--
					diag2[i+j]--
				}
			}
		}
	}
	_ = n
	return ans
}
