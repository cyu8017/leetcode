// LeetCode 3161 - Block Placement Queries
// https://leetcode.com/problems/block-placement-queries/

import "sort"

type fenwickMax struct {
	vals []int
}

func newFenwickMax(n int) *fenwickMax {
	return &fenwickMax{vals: make([]int, n+1)}
}

func (ft *fenwickMax) maximize(i, val int) {
	for i < len(ft.vals) {
		if val > ft.vals[i] {
			ft.vals[i] = val
		}
		i += i & -i
	}
}

func (ft *fenwickMax) get(i int) int {
	res := 0
	for i > 0 {
		if ft.vals[i] > res {
			res = ft.vals[i]
		}
		i -= i & -i
	}
	return res
}

func getResults(queries [][]int) []bool {
	n := len(queries) * 3
	if n > 50000 {
		n = 50000
	}
	tree := newFenwickMax(n + 1)
	obs := []int{0, n}
	for _, q := range queries {
		if q[0] == 1 {
			x := q[1]
			i := sort.SearchInts(obs, x)
			if i == len(obs) || obs[i] != x {
				obs = append(obs, 0)
				copy(obs[i+1:], obs[i:])
				obs[i] = x
			}
		}
	}
	for i := 0; i+1 < len(obs); i++ {
		tree.maximize(obs[i+1], obs[i+1]-obs[i])
	}

	ans := make([]bool, 0)
	for i := len(queries) - 1; i >= 0; i-- {
		typ, x := queries[i][0], queries[i][1]
		if typ == 1 {
			j := sort.SearchInts(obs, x)
			prev, next := obs[j-1], obs[j+1]
			obs = append(obs[:j], obs[j+1:]...)
			tree.maximize(next, next-prev)
		} else {
			sz := queries[i][2]
			j := sort.SearchInts(obs, x+1) - 1
			prev := obs[j]
			ans = append(ans, tree.get(prev) >= sz || x-prev >= sz)
		}
	}
	for i, j := 0, len(ans)-1; i < j; i, j = i+1, j-1 {
		ans[i], ans[j] = ans[j], ans[i]
	}
	return ans
}
