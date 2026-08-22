// LeetCode 3414 - Maximum Score of Non-overlapping Intervals
// https://leetcode.com/problems/maximum-score-of-non-overlapping-intervals/

import "sort"

func maximumWeight(intervals [][]int) []int {
	n := len(intervals)
	type it struct{ l, r, w, i int }
	arr := make([]it, n)
	for i, v := range intervals {
		arr[i] = it{v[0], v[1], v[2], i}
	}
	sort.Slice(arr, func(i, j int) bool { return arr[i].r < arr[j].r })
	// DP take up to 4
	type state struct {
		score int64
		idx   []int
	}
	better := func(a, b state) state {
		if a.score != b.score {
			if a.score > b.score {
				return a
			}
			return b
		}
		// lexicographically smaller idx
		for i := 0; i < len(a.idx) && i < len(b.idx); i++ {
			if a.idx[i] != b.idx[i] {
				if a.idx[i] < b.idx[i] {
					return a
				}
				return b
			}
		}
		if len(a.idx) <= len(b.idx) {
			return a
		}
		return b
	}
	dp := make([][]state, n+1)
	for i := range dp {
		dp[i] = make([]state, 5)
	}
	for i := 1; i <= n; i++ {
		cur := arr[i-1]
		for t := 0; t <= 4; t++ {
			dp[i][t] = dp[i-1][t]
		}
		// find previous non-overlap
		p := sort.Search(i-1, func(j int) bool { return arr[j].r >= cur.l })
		// p is first with r >= cur.l, so p-1 is last with r < cur.l
		prev := p
		for t := 1; t <= 4; t++ {
			prevState := dp[prev][t-1]
			newIdx := append(append([]int(nil), prevState.idx...), cur.i)
			sort.Ints(newIdx)
			cand := state{prevState.score + int64(cur.w), newIdx}
			dp[i][t] = better(dp[i][t], cand)
		}
	}
	best := dp[n][0]
	for t := 1; t <= 4; t++ {
		best = better(best, dp[n][t])
	}
	return best.idx
}
