// LeetCode 1040 - Moving Stones Until Consecutive II
// https://leetcode.com/problems/moving-stones-until-consecutive-ii/

import "sort"

func numMovesStonesII(stones []int) []int {
	sort.Ints(stones)
	n := len(stones)
	maxMoves := stones[n-1] - stones[1] - n + 2
	if v := stones[n-2] - stones[0] - n + 2; v > maxMoves {
		maxMoves = v
	}
	minMoves := maxMoves
	i := 0
	for j := 0; j < n; j++ {
		for stones[j]-stones[i]+1 > n {
			i++
		}
		inside := j - i + 1
		cur := n - inside
		if inside == n-1 && stones[j]-stones[i]+1 == n-1 {
			cur = 2
		}
		if cur < minMoves {
			minMoves = cur
		}
	}
	return []int{minMoves, maxMoves}
}
