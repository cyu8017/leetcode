// LeetCode 1054 - Distant Barcodes
// https://leetcode.com/problems/distant-barcodes/

import "sort"

func rearrangeBarcodes(barcodes []int) []int {
	count := map[int]int{}
	for _, v := range barcodes {
		count[v]++
	}
	type pair struct{ v, f int }
	pairs := make([]pair, 0, len(count))
	for v, f := range count {
		pairs = append(pairs, pair{v, f})
	}
	sort.Slice(pairs, func(i, j int) bool { return pairs[i].f > pairs[j].f })
	n := len(barcodes)
	ans := make([]int, n)
	idx := 0
	for _, p := range pairs {
		for k := 0; k < p.f; k++ {
			ans[idx] = p.v
			idx += 2
			if idx >= n {
				idx = 1
			}
		}
	}
	return ans
}
