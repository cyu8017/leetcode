// LeetCode 2838 - Maximum Coins Heroes Can Collect
// https://leetcode.com/problems/maximum-coins-heroes-can-collect/

import "sort"

func maximumCoins(heroes []int, monsters []int, coins []int) []int64 {
	n := len(monsters)
	idx := make([]int, n)
	for i := range idx {
		idx[i] = i
	}
	sort.Slice(idx, func(i, j int) bool { return monsters[idx[i]] < monsters[idx[j]] })
	pref := make([]int64, n+1)
	ms := make([]int, n)
	for i, id := range idx {
		ms[i] = monsters[id]
		pref[i+1] = pref[i] + int64(coins[id])
	}
	ans := make([]int64, len(heroes))
	for i, h := range heroes {
		p := sort.Search(n, func(j int) bool { return ms[j] > h })
		ans[i] = pref[p]
	}
	return ans
}
