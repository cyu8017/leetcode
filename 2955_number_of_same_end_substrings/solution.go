// LeetCode 2955 - Number of Same-End Substrings
// https://leetcode.com/problems/number-of-same-end-substrings/

func sameEndSubstringCount(s string, queries [][]int) []int {
	n := len(s)
	pref := make([][26]int, n+1)
	for i := 0; i < n; i++ {
		pref[i+1] = pref[i]
		pref[i+1][s[i]-'a']++
	}
	ans := make([]int, len(queries))
	for qi, q := range queries {
		l, r := q[0], q[1]
		total := 0
		for c := 0; c < 26; c++ {
			cnt := pref[r+1][c] - pref[l][c]
			total += cnt * (cnt + 1) / 2
		}
		ans[qi] = total
	}
	return ans
}
