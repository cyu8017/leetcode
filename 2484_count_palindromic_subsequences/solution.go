// LeetCode 2484 - Count Palindromic Subsequences
// https://leetcode.com/problems/count-palindromic-subsequences/

func countPalindromes(s string) int {
	const mod = 1000000007
	n := len(s)
	pref := make([][10][10]int, n)
	cnt := [10]int{}
	for i := 0; i < n; i++ {
		if i > 0 {
			pref[i] = pref[i-1]
		}
		d := int(s[i] - '0')
		for a := 0; a < 10; a++ {
			pref[i][a][d] += cnt[a]
		}
		cnt[d]++
	}
	suf := make([][10][10]int, n)
	cnt = [10]int{}
	for i := n - 1; i >= 0; i-- {
		if i+1 < n {
			suf[i] = suf[i+1]
		}
		d := int(s[i] - '0')
		for a := 0; a < 10; a++ {
			suf[i][a][d] += cnt[a]
		}
		cnt[d]++
	}
	ans := 0
	for i := 2; i < n-2; i++ {
		for a := 0; a < 10; a++ {
			for b := 0; b < 10; b++ {
				ans = (ans + pref[i-1][a][b]*suf[i+1][a][b]) % mod
			}
		}
	}
	return ans
}
