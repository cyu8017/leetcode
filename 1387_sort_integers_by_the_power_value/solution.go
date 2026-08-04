// LeetCode 1387 - Sort Integers by The Power Value
// https://leetcode.com/problems/sort-integers-by-the-power-value/

import "sort"

func getKth(lo int, hi int, k int) int {
	memo := map[int]int{}
	var power func(int) int
	power = func(x int) int {
		if x == 1 {
			return 0
		}
		if v, ok := memo[x]; ok {
			return v
		}
		var nxt int
		if x%2 == 0 {
			nxt = x / 2
		} else {
			nxt = 3*x + 1
		}
		memo[x] = 1 + power(nxt)
		return memo[x]
	}
	vals := make([]int, 0, hi-lo+1)
	for x := lo; x <= hi; x++ {
		vals = append(vals, x)
	}
	sort.Slice(vals, func(i, j int) bool {
		pi, pj := power(vals[i]), power(vals[j])
		if pi != pj {
			return pi < pj
		}
		return vals[i] < vals[j]
	})
	return vals[k-1]
}
