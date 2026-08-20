// LeetCode 0954 - Array of Doubled Pairs
// https://leetcode.com/problems/array-of-doubled-pairs/

import "sort"

func canReorderDoubled(arr []int) bool {
	count := map[int]int{}
	keys := []int{}
	for _, x := range arr {
		if count[x] == 0 {
			keys = append(keys, x)
		}
		count[x]++
	}
	sort.Slice(keys, func(i, j int) bool {
		ai, aj := keys[i], keys[j]
		if ai < 0 {
			ai = -ai
		}
		if aj < 0 {
			aj = -aj
		}
		return ai < aj
	})
	for _, x := range keys {
		if count[x] == 0 {
			continue
		}
		if count[2*x] < count[x] {
			return false
		}
		count[2*x] -= count[x]
	}
	return true
}
