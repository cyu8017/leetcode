// LeetCode 1140 - Stone Game II
// https://leetcode.com/problems/stone-game-ii/

func stoneGameII(piles []int) int {
	n := len(piles)
	suffix := make([]int, n+1)
	for i := n - 1; i >= 0; i-- {
		suffix[i] = suffix[i+1] + piles[i]
	}
	memo := make([][]int, n)
	for i := range memo {
		memo[i] = make([]int, n+1)
		for j := range memo[i] {
			memo[i][j] = -1
		}
	}
	var dp func(int, int) int
	dp = func(i, m int) int {
		if i >= n {
			return 0
		}
		if memo[i][m] != -1 {
			return memo[i][m]
		}
		best := 0
		for x := 1; x <= 2*m && i+x-1 < n; x++ {
			v := suffix[i] - dp(i+x, max(m, x))
			if v > best {
				best = v
			}
		}
		memo[i][m] = best
		return best
	}
	return dp(0, 1)
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}
