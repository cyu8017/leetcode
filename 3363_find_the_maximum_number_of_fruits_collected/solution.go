// LeetCode 3363 - Find the Maximum Number of Fruits Collected
// https://leetcode.com/problems/find-the-maximum-number-of-fruits-collected/

func maxCollectedFruits(fruits [][]int) int {
	n := len(fruits)
	ans := 0
	for i := 0; i < n; i++ {
		ans += fruits[i][i]
		fruits[i][i] = 0
	}
	// child2 from (0,n-1) moves down-ish
	const neg = -1 << 30
	dp2 := make([][]int, n)
	dp3 := make([][]int, n)
	for i := range dp2 {
		dp2[i] = make([]int, n)
		dp3[i] = make([]int, n)
		for j := range dp2[i] {
			dp2[i][j] = neg
			dp3[i][j] = neg
		}
	}
	dp2[0][n-1] = fruits[0][n-1]
	for i := 0; i < n; i++ {
		for j := 0; j < n; j++ {
			if dp2[i][j] == neg {
				continue
			}
			for _, dj := range []int{-1, 0, 1} {
				ni, nj := i+1, j+dj
				if ni < n && nj >= 0 && nj < n && nj > ni {
					v := dp2[i][j] + fruits[ni][nj]
					if v > dp2[ni][nj] {
						dp2[ni][nj] = v
					}
				}
			}
		}
	}
	dp3[n-1][0] = fruits[n-1][0]
	for j := 0; j < n; j++ {
		for i := 0; i < n; i++ {
			if dp3[i][j] == neg {
				continue
			}
			for _, di := range []int{-1, 0, 1} {
				ni, nj := i+di, j+1
				if ni >= 0 && ni < n && nj < n && ni > nj {
					v := dp3[i][j] + fruits[ni][nj]
					if v > dp3[ni][nj] {
						dp3[ni][nj] = v
					}
				}
			}
		}
	}
	ans += dp2[n-1][n-1] + dp3[n-1][n-1]
	return ans
}
