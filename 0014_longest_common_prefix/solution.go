// LeetCode 0014 - Longest Common Prefix
// https://leetcode.com/problems/longest-common-prefix/

func longestCommonPrefix(strs []string) string {
	if len(strs) == 0 {
		return ""
	}

	for i := 0; i < len(strs[0]); i++ {
		ch := strs[0][i]
		for j := 1; j < len(strs); j++ {
			if i >= len(strs[j]) || strs[j][i] != ch {
				return strs[0][:i]
			}
		}
	}

	return strs[0]
}
