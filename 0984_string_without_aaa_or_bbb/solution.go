// LeetCode 0984 - String Without AAA or BBB
// https://leetcode.com/problems/string-without-aaa-or-bbb/

func strWithout3a3b(a int, b int) string {
	ans := []byte{}
	for a > 0 || b > 0 {
		writeA := false
		if len(ans) >= 2 && ans[len(ans)-1] == ans[len(ans)-2] {
			writeA = ans[len(ans)-1] == 'b'
		} else {
			writeA = a >= b
		}
		if writeA {
			ans = append(ans, 'a')
			a--
		} else {
			ans = append(ans, 'b')
			b--
		}
	}
	return string(ans)
}
