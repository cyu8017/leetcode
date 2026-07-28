// LeetCode 1039 - Minimum Score Triangulation of Polygon
// https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

func minScoreTriangulation(values []int) int {
	n := len(values)
	memo := make([][]int, n)
	for i := range memo {
		memo[i] = make([]int, n)
		for j := range memo[i] {
			memo[i][j] = -1
		}
	}
	var dp func(i, j int) int
	dp = func(i, j int) int {
		if j-i < 2 {
			return 0
		}
		if memo[i][j] != -1 {
			return memo[i][j]
		}
		best := int(^uint(0) >> 1)
		for k := i + 1; k < j; k++ {
			v := dp(i, k) + values[i]*values[k]*values[j] + dp(k, j)
			if v < best {
				best = v
			}
		}
		memo[i][j] = best
		return best
	}
	return dp(0, n-1)
}
