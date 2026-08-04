// LeetCode 1163 - Last Substring in Lexicographical Order
// https://leetcode.com/problems/last-substring-in-lexicographical-order/

func lastSubstring(s string) string {
	i, j, k := 0, 1, 0
	n := len(s)
	for j+k < n {
		if s[i+k] == s[j+k] {
			k++
			continue
		}
		if s[i+k] < s[j+k] {
			i += k + 1
			if i <= j {
				i = j
			}
			j = i + 1
		} else {
			j += k + 1
		}
		k = 0
		if j <= i {
			j = i + 1
		}
	}
	return s[i:]
}
