// LeetCode 1388 - Pizza With 3n Slices
// https://leetcode.com/problems/pizza-with-3n-slices/

func maxSizeSlices(slices []int) int {
	k := len(slices) / 3
	line := func(a []int) int {
		dp := make([][]int, len(a)+2)
		for i := range dp {
			dp[i] = make([]int, k+1)
		}
		for i, x := range a {
			ii := i + 2
			for j := 1; j <= k; j++ {
				v := dp[ii-1][j]
				alt := dp[ii-2][j-1] + x
				if alt > v {
					v = alt
				}
				dp[ii][j] = v
			}
		}
		return dp[len(a)+1][k]
	}
	a := line(slices[:len(slices)-1])
	b := line(slices[1:])
	if a > b {
		return a
	}
	return b
}
