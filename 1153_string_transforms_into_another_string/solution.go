// LeetCode 1153 - String Transforms Into Another String
// https://leetcode.com/problems/string-transforms-into-another-string/

func canConvert(str1 string, str2 string) bool {
	if str1 == str2 {
		return true
	}
	mapping := map[byte]byte{}
	for i := 0; i < len(str1); i++ {
		a, b := str1[i], str2[i]
		if v, ok := mapping[a]; ok && v != b {
			return false
		}
		mapping[a] = b
	}
	seen := map[byte]bool{}
	for i := 0; i < len(str2); i++ {
		seen[str2[i]] = true
	}
	return len(seen) < 26
}
