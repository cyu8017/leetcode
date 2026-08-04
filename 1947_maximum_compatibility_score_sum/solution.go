// LeetCode 1947 - Maximum Compatibility Score Sum
// https://leetcode.com/problems/maximum-compatibility-score-sum/

func maxCompatibilitySum(students [][]int, mentors [][]int) int {
	m := len(students)
	score := make([][]int, m)
	for i := 0; i < m; i++ {
		score[i] = make([]int, m)
		for j := 0; j < m; j++ {
			for k := range students[i] {
				if students[i][k] == mentors[j][k] {
					score[i][j]++
				}
			}
		}
	}
	memo := make(map[[2]int]int)
	var dp func(i, mask int) int
	dp = func(i, mask int) int {
		if i == m {
			return 0
		}
		key := [2]int{i, mask}
		if v, ok := memo[key]; ok {
			return v
		}
		best := 0
		for j := 0; j < m; j++ {
			if mask&(1<<j) == 0 {
				v := score[i][j] + dp(i+1, mask|(1<<j))
				if v > best {
					best = v
				}
			}
		}
		memo[key] = best
		return best
	}
	return dp(0, 0)
}
