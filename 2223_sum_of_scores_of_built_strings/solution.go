// LeetCode 2223 - Sum of Scores of Built Strings
// https://leetcode.com/problems/sum-of-scores-of-built-strings/

func sumScores(s string) int64 {
	n := len(s)
	z := make([]int, n)
	l, r := 0, 0
	for i := 1; i < n; i++ {
		if i <= r {
			z[i] = z[i-l]
			if r-i+1 < z[i] {
				z[i] = r - i + 1
			}
		}
		for i+z[i] < n && s[z[i]] == s[i+z[i]] {
			z[i]++
		}
		if i+z[i]-1 > r {
			l, r = i, i+z[i]-1
		}
	}
	var ans int64 = int64(n)
	for i := 1; i < n; i++ {
		ans += int64(z[i])
	}
	return ans
}
