// LeetCode 0953 - Verifying an Alien Dictionary
// https://leetcode.com/problems/verifying-an-alien-dictionary/

func isAlienSorted(words []string, order string) bool {
	rank := make([]int, 26)
	for i, c := range order {
		rank[c-'a'] = i
	}
	lessEq := func(a, b string) bool {
		n := len(a)
		if len(b) < n {
			n = len(b)
		}
		for i := 0; i < n; i++ {
			ra, rb := rank[a[i]-'a'], rank[b[i]-'a']
			if ra < rb {
				return true
			}
			if ra > rb {
				return false
			}
		}
		return len(a) <= len(b)
	}
	for i := 0; i < len(words)-1; i++ {
		if !lessEq(words[i], words[i+1]) {
			return false
		}
	}
	return true
}
