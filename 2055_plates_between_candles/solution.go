// LeetCode 2055 - Plates Between Candles
// https://leetcode.com/problems/plates-between-candles/

func platesBetweenCandles(s string, queries [][]int) []int {
	n := len(s)
	pref := make([]int, n+1)
	left := make([]int, n)
	right := make([]int, n)
	last := -1
	for i := 0; i < n; i++ {
		pref[i+1] = pref[i]
		if s[i] == '*' {
			pref[i+1]++
		} else {
			last = i
		}
		left[i] = last
	}
	last = -1
	for i := n - 1; i >= 0; i-- {
		if s[i] == '|' {
			last = i
		}
		right[i] = last
	}
	ans := make([]int, len(queries))
	for i, q := range queries {
		l, r := right[q[0]], left[q[1]]
		if l != -1 && r != -1 && l < r {
			ans[i] = pref[r] - pref[l]
		}
	}
	return ans
}
