// LeetCode 2983 - Palindrome Rearrangement Queries
// https://leetcode.com/problems/palindrome-rearrangement-queries/

func canMakePalindromeQueries(s string, queries [][]int) []bool {
	n := len(s)
	half := n / 2
	pref := make([][26]int, half+1)
	for i := 0; i < half; i++ {
		pref[i+1] = pref[i]
		pref[i+1][s[i]-'a']++
		pref[i+1][s[n-1-i]-'a']--
	}
	diffPref := make([]int, half+1)
	for i := 0; i < half; i++ {
		d := 0
		if s[i] != s[n-1-i] {
			d = 1
		}
		diffPref[i+1] = diffPref[i] + d
	}
	ans := make([]bool, len(queries))
	for qi, q := range queries {
		a, b, c, d := q[0], q[1], q[2], q[3]
		c2, d2 := n-1-d, n-1-c
		// check outside rearrange regions match
		ok := true
		// simplified: count freq in rearrangeable positions must match
		freq := [26]int{}
		mark := make([]bool, n)
		for i := a; i <= b; i++ {
			mark[i] = true
		}
		for i := c; i <= d; i++ {
			mark[i] = true
		}
		for i := 0; i < half; i++ {
			j := n - 1 - i
			if !mark[i] && !mark[j] {
				if s[i] != s[j] {
					ok = false
					break
				}
			} else {
				if mark[i] {
					freq[s[i]-'a']++
				} else {
					freq[s[i]-'a']--
				}
				if mark[j] {
					freq[s[j]-'a']++
				} else {
					freq[s[j]-'a']--
				}
			}
		}
		if ok {
			for _, f := range freq {
				if f != 0 {
					ok = false
					break
				}
			}
		}
		_ = c2
		_ = d2
		_ = pref
		_ = diffPref
		ans[qi] = ok
	}
	return ans
}
