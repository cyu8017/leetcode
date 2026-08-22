// LeetCode 3424 - Minimum Cost to Make Arrays Identical
// https://leetcode.com/problems/minimum-cost-to-make-arrays-identical/

import "sort"

func minCost(arr []int, brr []int, k int64) int64 {
	var noSwap int64
	for i := range arr {
		d := arr[i] - brr[i]
		if d < 0 {
			d = -d
		}
		noSwap += int64(d)
	}
	a2 := append([]int(nil), arr...)
	b2 := append([]int(nil), brr...)
	sort.Ints(a2)
	sort.Ints(b2)
	var withSwap int64 = k
	for i := range a2 {
		d := a2[i] - b2[i]
		if d < 0 {
			d = -d
		}
		withSwap += int64(d)
	}
	if noSwap < withSwap {
		return noSwap
	}
	return withSwap
}
