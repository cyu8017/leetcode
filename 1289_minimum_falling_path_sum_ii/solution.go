// LeetCode 1289 - Minimum Falling Path Sum II
// https://leetcode.com/problems/minimum-falling-path-sum-ii/

func minFallingPathSum(grid [][]int) int {
	dp := append([]int{}, grid[0]...)
	for _, row := range grid[1:] {
		first := 0
		for i := 1; i < len(dp); i++ {
			if dp[i] < dp[first] {
				first = i
			}
		}
		secondValue := 0
		if len(dp) > 1 {
			secondValue = int(^uint(0) >> 1)
			for i := 0; i < len(dp); i++ {
				if i != first && dp[i] < secondValue {
					secondValue = dp[i]
				}
			}
		}
		nxt := make([]int, len(row))
		for i, value := range row {
			if i == first {
				nxt[i] = value + secondValue
			} else {
				nxt[i] = value + dp[first]
			}
		}
		dp = nxt
	}
	best := dp[0]
	for _, v := range dp[1:] {
		if v < best {
			best = v
		}
	}
	return best
}
