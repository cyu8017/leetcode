// LeetCode 2375 - Construct Smallest Number From DI String
// https://leetcode.com/problems/construct-smallest-number-from-di-string/

func smallestNumber(pattern string) string {
	n := len(pattern)
	ans := make([]byte, n+1)
	for i := 0; i <= n; i++ {
		ans[i] = byte('1' + i)
	}
	i := 0
	for i < n {
		if pattern[i] == 'I' {
			i++
			continue
		}
		j := i
		for j < n && pattern[j] == 'D' {
			j++
		}
		l, r := i, j
		for l < r {
			ans[l], ans[r] = ans[r], ans[l]
			l++
			r--
		}
		i = j
	}
	return string(ans)
}
