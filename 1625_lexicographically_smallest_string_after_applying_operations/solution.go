// LeetCode 1625 - Lexicographically Smallest String After Applying Operations
// https://leetcode.com/problems/lexicographically-smallest-string-after-applying-operations/

func findLexSmallestString(s string, a int, b int) string {
	seen := map[string]bool{s: true}
	q := []string{s}
	ans := s
	for len(q) > 0 {
		cur := q[0]
		q = q[1:]
		if cur < ans {
			ans = cur
		}
		bytes := []byte(cur)
		for i := 1; i < len(bytes); i += 2 {
			bytes[i] = byte((int(bytes[i]-'0')+a)%10 + '0')
		}
		add := string(bytes)
		rot := cur[len(cur)-b:] + cur[:len(cur)-b]
		for _, nxt := range []string{add, rot} {
			if !seen[nxt] {
				seen[nxt] = true
				q = append(q, nxt)
			}
		}
	}
	return ans
}
