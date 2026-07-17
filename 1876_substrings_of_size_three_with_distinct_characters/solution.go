// LeetCode 1876 - Substrings of Size Three with Distinct Characters
// https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/

func countGoodSubstrings(s string) int {
	if len(s) < 3 {
		return 0
	}

	count := 0
	for i := 0; i <= len(s)-3; i++ {
		window := s[i : i+3]
		seen := make(map[byte]struct{}, 3)
		for j := 0; j < 3; j++ {
			seen[window[j]] = struct{}{}
		}
		if len(seen) == 3 {
			count++
		}
	}
	return count
}
