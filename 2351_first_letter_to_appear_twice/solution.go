// LeetCode 2351 - First Letter to Appear Twice
// https://leetcode.com/problems/first-letter-to-appear-twice/

func repeatedCharacter(s string) byte {
	seen := [26]bool{}
	for i := 0; i < len(s); i++ {
		c := s[i] - 'a'
		if seen[c] {
			return s[i]
		}
		seen[c] = true
	}
	return 0
}
