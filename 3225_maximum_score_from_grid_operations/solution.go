// LeetCode 3225 - Maximum Score From Grid Operations
// https://leetcode.com/problems/maximum-score-from-grid-operations/

func maximumScore(grid [][]int) int64 {
	n := len(grid)
	prefix := make([][]int64, n)
	for j := 0; j < n; j++ {
		prefix[j] = make([]int64, n+1)
		for i := 0; i < n; i++ {
			prefix[j][i+1] = prefix[j][i] + int64(grid[i][j])
		}
	}
	prevPick := make([]int64, n+1)
	prevSkip := make([]int64, n+1)
	for j := 1; j < n; j++ {
		currPick := make([]int64, n+1)
		currSkip := make([]int64, n+1)
		for curr := 0; curr <= n; curr++ {
			for prev := 0; prev <= n; prev++ {
				if curr > prev {
					score := prefix[j-1][curr] - prefix[j-1][prev]
					if prevSkip[prev]+score > currPick[curr] {
						currPick[curr] = prevSkip[prev] + score
					}
					if prevSkip[prev]+score > currSkip[curr] {
						currSkip[curr] = prevSkip[prev] + score
					}
				} else {
					score := prefix[j][prev] - prefix[j][curr]
					if prevPick[prev]+score > currPick[curr] {
						currPick[curr] = prevPick[prev] + score
					}
					if prevPick[prev] > currSkip[curr] {
						currSkip[curr] = prevPick[prev]
					}
				}
			}
		}
		prevPick, prevSkip = currPick, currSkip
	}
	ans := prevPick[0]
	for _, v := range prevPick {
		if v > ans {
			ans = v
		}
	}
	return ans
}
