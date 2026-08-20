// LeetCode 2301 - Match Substring After Replacement
// https://leetcode.com/problems/match-substring-after-replacement/

func matchReplacement(s string, sub string, mappings [][]byte) bool {
	allow := map[[2]byte]bool{}
	for _, m := range mappings {
		allow[[2]byte{m[0], m[1]}] = true
	}
	n, m := len(s), len(sub)
	for i := 0; i+m <= n; i++ {
		ok := true
		for j := 0; j < m; j++ {
			a, b := s[i+j], sub[j]
			if a == b || allow[[2]byte{b, a}] {
				continue
			}
			ok = false
			break
		}
		if ok {
			return true
		}
	}
	return false
}
