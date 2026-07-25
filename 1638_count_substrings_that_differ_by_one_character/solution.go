// LeetCode 1638 - Count Substrings That Differ by One Character
// https://leetcode.com/problems/count-substrings-that-differ-by-one-character/

func countSubstrings(s string, t string) int {
	ans := 0
	for i := 0; i < len(s); i++ {
		for j := 0; j < len(t); j++ {
			diff := 0
			for k := 0; i+k < len(s) && j+k < len(t); k++ {
				if s[i+k] != t[j+k] {
					diff++
				}
				if diff == 1 {
					ans++
				} else if diff > 1 {
					break
				}
			}
		}
	}
	return ans
}
