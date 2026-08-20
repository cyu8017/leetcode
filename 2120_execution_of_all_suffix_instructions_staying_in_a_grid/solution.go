// LeetCode 2120 - Execution of All Suffix Instructions Staying in a Grid
// https://leetcode.com/problems/execution-of-all-suffix-instructions-staying-in-a-grid/

func executeInstructions(n int, startPos []int, s string) []int {
	m := len(s)
	ans := make([]int, m)
	for i := 0; i < m; i++ {
		r, c := startPos[0], startPos[1]
		cnt := 0
		for j := i; j < m; j++ {
			switch s[j] {
			case 'L':
				c--
			case 'R':
				c++
			case 'U':
				r--
			case 'D':
				r++
			}
			if r < 0 || r >= n || c < 0 || c >= n {
				break
			}
			cnt++
		}
		ans[i] = cnt
	}
	return ans
}
