// LeetCode 3106 - Lexicographically Smallest String After Operations With Constraint
// https://leetcode.com/problems/lexicographically-smallest-string-after-operations-with-constraint/

func getSmallestString(s string, k int) string {
	cs := []byte(s)
	for i, c1 := range cs {
		for c2 := byte('a'); c2 < c1; c2++ {
			d := int(min(c1-c2, 26-c1+c2))
			if d <= k {
				cs[i] = c2
				k -= d
				break
			}
		}
	}
	return string(cs)
}
