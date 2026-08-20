// LeetCode 2546 - Apply Bitwise Operations to Make Strings Equal
// https://leetcode.com/problems/apply-bitwise-operations-to-make-strings-equal/


func makeStringsEqual(s string, target string) bool {
	has1s, has1t := false, false
	for i := 0; i < len(s); i++ {
		if s[i] == '1' {
			has1s = true
		}
		if target[i] == '1' {
			has1t = true
		}
	}
	return has1s == has1t
}
