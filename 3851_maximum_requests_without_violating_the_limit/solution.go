// LeetCode 3851 - Maximum Requests Without Violating The Limit
// https://leetcode.com/problems/maximum-requests-without-violating-the-limit/

import "sort"

func maxRequests(requests [][]int, k int, window int) int {
	g := make(map[int][]int)
	for _, r := range requests {
		u, t := r[0], r[1]
		g[u] = append(g[u], t)
	}
	ans := len(requests)
	for _, ts := range g {
		sort.Ints(ts)
		kept := make([]int, 0)
		for _, t := range ts {
			for len(kept) > 0 && t-kept[0] > window {
				kept = kept[1:]
			}
			if len(kept) < k {
				kept = append(kept, t)
			} else {
				ans--
			}
		}
	}
	return ans
}
