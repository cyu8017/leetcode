// LeetCode 3594 - Minimum Time to Transport All Individuals
// https://leetcode.com/problems/minimum-time-to-transport-all-individuals/

import "sort"

func minTime(n int, k int, m int, time []int, mul []float64) float64 {
	t := append([]int(nil), time...)
	sort.Ints(t)
	total := 0.0
	stage := 0
	left := n
	for left > 0 {
		take := k
		if take > left {
			take = left
		}
		slow := t[left-1]
		total += float64(slow) * mul[stage%m]
		left -= take
		stage++
		if left > 0 {
			total += float64(t[0]) * mul[stage%m]
			stage++
		}
	}
	return total
}
