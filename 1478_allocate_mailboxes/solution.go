// LeetCode 1478 - Allocate Mailboxes
// https://leetcode.com/problems/allocate-mailboxes/

import "sort"

func minDistance(houses []int, k int) int {
	sort.Ints(houses)
	n := len(houses)
	cost := make([][]int, n)
	for i := range cost {
		cost[i] = make([]int, n)
		for j := i; j < n; j++ {
			mid := houses[(i+j)/2]
			s := 0
			for t := i; t <= j; t++ {
				d := houses[t] - mid
				if d < 0 {
					d = -d
				}
				s += d
			}
			cost[i][j] = s
		}
	}
	const inf = int(1e15)
	dp := make([]int, n+1)
	dp[0] = 0
	for i := 1; i <= n; i++ {
		dp[i] = inf
	}
	for mb := 0; mb < k; mb++ {
		ndp := make([]int, n+1)
		ndp[0] = 0
		for i := 1; i <= n; i++ {
			ndp[i] = inf
		}
		for j := 1; j <= n; j++ {
			for i := 0; i < j; i++ {
				v := dp[i] + cost[i][j-1]
				if v < ndp[j] {
					ndp[j] = v
				}
			}
		}
		dp = ndp
	}
	return dp[n]
}
