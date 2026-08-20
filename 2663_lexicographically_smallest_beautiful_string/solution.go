// LeetCode 2663 - Lexicographically Smallest Beautiful String
// https://leetcode.com/problems/lexicographically-smallest-beautiful-string/


func smallestBeautifulString(s string, k int) string {
	n := len(s)
	b := []byte(s)
	for i := n - 1; i >= 0; i-- {
		for c := b[i] + 1; c < byte('a'+k); c++ {
			if (i > 0 && c == b[i-1]) || (i > 1 && c == b[i-2]) {
				continue
			}
			b[i] = c
			for j := i + 1; j < n; j++ {
				for nc := byte('a'); nc < byte('a'+k); nc++ {
					if (j > 0 && nc == b[j-1]) || (j > 1 && nc == b[j-2]) {
						continue
					}
					b[j] = nc
					break
				}
			}
			return string(b)
		}
	}
	return ""
}
