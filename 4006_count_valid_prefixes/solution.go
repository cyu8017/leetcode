// LeetCode 4006 - Count Valid Prefixes
// https://leetcode.com/problems/count-valid-prefixes/

func countValidPrefixes(s string) int {
	ans, t := 0, 0
	for _, c := range s {
		if c == '1' {
			t++
		} else {
			t--
		}
		if t >= -1 && t <= 1 {
			ans++
		}
	}
	return ans
}
